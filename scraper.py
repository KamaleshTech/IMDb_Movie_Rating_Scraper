from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.imdb.com/chart/top/")
time.sleep(5)

movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
print("Movies found:", len(movies))

data = []

for rank, movie in enumerate(movies, start=1):
    try:
        title = movie.find_element(By.TAG_NAME, "h3").text.strip()

        rating = movie.find_element(
            By.CSS_SELECTOR, "span.ipc-rating-star--rating"
        ).text.strip()

        year = "N/A"

        # 1) Try the visible metadata spans first
        metadata = movie.find_elements(By.CSS_SELECTOR, "span.cli-title-metadata-item")
        for item in metadata:
            txt = item.text.strip()
            if re.fullmatch(r"(19|20)\d{2}", txt):
                year = txt
                break

        # 2) Fallback: search the full HTML for a 4-digit year
        if year == "N/A":
            html = movie.get_attribute("outerHTML")
            match = re.search(r">\s*((?:19|20)\d{2})\s*<", html)
            if match:
                year = match.group(1)

        # 3) Final fallback: search the visible text
        if year == "N/A":
            text = movie.text
            match = re.search(r"\b((?:19|20)\d{2})\b", text)
            if match:
                year = match.group(1)

        data.append([rank, title, year, rating])

    except Exception as e:
        print(f"Error in rank {rank}: {e}")

df = pd.DataFrame(data, columns=["Rank", "Title", "Year", "Rating"])
df.to_csv("movies.csv", index=False)

driver.quit()