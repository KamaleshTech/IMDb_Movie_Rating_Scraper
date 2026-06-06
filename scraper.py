from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.imdb.com/chart/top/")

wait = WebDriverWait(driver, 20)
wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
    )
)

movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
print("Movies found:", len(movies))

data = []

for rank, movie in enumerate(movies, start=1):
    try:
        title = None
        year = "N/A"
        rating = "N/A"

        # 1) Best guess for title from IMDb's title link
        title_selectors = [
            "a.ipc-title-link-wrapper h3.ipc-title__text",
            "a.ipc-title-link-wrapper",
            "h3.ipc-title__text",
            "h3"
        ]

        for sel in title_selectors:
            els = movie.find_elements(By.CSS_SELECTOR, sel)
            if els:
                txt = els[0].text.strip()
                if txt:
                    # remove leading rank-like text such as "#1" or "1."
                    txt = re.sub(r"^\s*(?:#\d+\s*|\d+\.\s*)", "", txt).strip()
                    if txt and not re.fullmatch(r"#?\d+", txt):
                        title = txt
                        break

        # 2) Fallback: parse visible row text
        text = movie.text.strip()
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]

        if not title:
            # pick the first line that actually looks like a movie title
            for ln in lines:
                if re.fullmatch(r"#?\d+", ln):
                    continue
                if re.fullmatch(r"(19|20)\d{2}", ln):
                    continue
                if re.fullmatch(r"\d\.\d", ln):
                    continue
                if any(ch.isalpha() for ch in ln):
                    title = re.sub(r"^\s*(?:#\d+\s*|\d+\.\s*)", "", ln).strip()
                    break

        if not title:
            continue

        # Rating
        rating_selectors = [
            "span.ipc-rating-star--rating",
            "span.ipc-rating-star",
        ]
        for sel in rating_selectors:
            els = movie.find_elements(By.CSS_SELECTOR, sel)
            if els:
                rtxt = els[0].text.strip()
                if rtxt:
                    m = re.search(r"\d\.\d", rtxt)
                    if m:
                        rating = m.group()
                        break

        if rating == "N/A":
            m = re.search(r"\b(\d\.\d)\b", text)
            if m:
                rating = m.group(1)

        # Year
        metadata = movie.find_elements(By.CSS_SELECTOR, "span.cli-title-metadata-item")
        for item in metadata:
            txt = item.text.strip()
            if re.fullmatch(r"(19|20)\d{2}", txt):
                year = txt
                break

        if year == "N/A":
            m = re.search(r"\b((?:19|20)\d{2})\b", text)
            if m:
                year = m.group(1)

        data.append([rank, title, year, rating])

    except Exception as e:
        print(f"Error in rank {rank}: {e}")

df = pd.DataFrame(data, columns=["Rank", "Title", "Year", "Rating"])
df.to_csv("movies.csv", index=False, encoding="utf-8-sig")

print("Saved to movies.csv")
print("Rows saved:", len(df))

driver.quit()