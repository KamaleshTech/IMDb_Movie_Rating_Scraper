from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

URL = "https://www.imdb.com/chart/top/"

def clean_title(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r"^\s*#?\d+\s*[\.\)]?\s*", "", raw)   # remove leading rank
    raw = re.sub(r"\s*\(\d{4}\)\s*$", "", raw)         # remove trailing year if present
    return raw.strip()

def extract_year(text: str, html: str) -> str:
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text)
    if m:
        return m.group(1)
    m = re.search(r"\b(19\d{2}|20\d{2})\b", html)
    if m:
        return m.group(1)
    return "N/A"

def extract_rating(text: str, html: str) -> str:
    m = re.search(r"\b(\d\.\d)\b", text)
    if m:
        return m.group(1)
    m = re.search(r'ipc-rating-star--rating[^>]*>\s*([\d.]+)\s*<', html)
    if m:
        return m.group(1)
    return "N/A"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)
driver.get(URL)

wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
    )
)

rows = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
print("Movies found:", len(rows))

data = []

for rank, row in enumerate(rows, start=1):
    try:
        text = row.text.strip()
        html = row.get_attribute("outerHTML") or ""

        if not text:
            continue

        # Title: try the title header/link first
        title = None
        title_candidates = row.find_elements(
            By.CSS_SELECTOR,
            "a.ipc-title-link-wrapper h3.ipc-title__text, h3.ipc-title__text, a.ipc-title-link-wrapper"
        )

        for el in title_candidates:
            candidate = el.text.strip()
            if candidate:
                title = clean_title(candidate)
                break

        # Fallback: first meaningful visible line
        if not title:
            lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
            for ln in lines:
                if re.fullmatch(r"#?\d+", ln):
                    continue
                if re.fullmatch(r"(19\d{2}|20\d{2})", ln):
                    continue
                if re.fullmatch(r"\d\.\d", ln):
                    continue
                if any(ch.isalpha() for ch in ln):
                    title = clean_title(ln)
                    break

        if not title:
            continue

        year = extract_year(text, html)
        rating = extract_rating(text, html)

        data.append([rank, title, year, rating])

    except Exception as e:
        print(f"Skipping rank {rank}: {e}")

df = pd.DataFrame(data, columns=["Rank", "Title", "Year", "Rating"])
df.to_csv("movies.csv", index=False, encoding="utf-8-sig")

print("Saved to movies.csv")
print("Rows saved:", len(df))

driver.quit()