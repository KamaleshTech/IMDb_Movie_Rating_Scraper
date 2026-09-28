# 🎬 IMDb Movie Rating Scraper

### Automated IMDb Top 250 Movie Data Extraction using Python & Selenium

A Python-based web scraping project that automates the collection of IMDb Top 250 movie information using Selenium and Chrome WebDriver.

The scraper extracts movie rankings, titles, release years, and IMDb ratings, processes the collected data using Pandas, and stores the results in CSV format. A simple web dashboard is also included to display and search the scraped movie data.

---

## 📌 About

**IMDb Movie Rating Scraper** is a web scraping project developed to automate the extraction of structured movie information from IMDb.

The project uses **Selenium WebDriver** to interact with dynamically rendered web pages and collect movie details.

The extracted data is processed using **Pandas** and stored in a CSV file. A lightweight web dashboard is included to present the collected IMDb Top 250 movie data in a clean and searchable interface.

---

## ✨ Features

- 🎬 **IMDb Top 250 Scraping** — Extracts movie information from IMDb
- 🏆 **Ranking Extraction** — Captures the ranking of each movie
- 🎞️ **Movie Details** — Extracts movie titles and release years
- ⭐ **Rating Extraction** — Collects IMDb ratings
- 🤖 **Browser Automation** — Uses Selenium with Chrome WebDriver
- 📊 **Data Processing** — Processes extracted data using Pandas
- 📁 **CSV Export** — Stores scraped data in `movies.csv`
- 🔎 **Movie Search** — Search movies through the dashboard
- 🌐 **Web Dashboard** — Displays the collected movie data

---

## 🛠️ Technologies

**Programming:** Python

**Web Scraping:** Selenium, WebDriver Manager

**Data Processing:** Pandas

**Browser:** Google Chrome

**Frontend:** HTML, CSS, JavaScript

**Data Storage:** CSV

**Deployment:** Vercel

---

## 🔄 Workflow

```text
IMDb Top 250 Page
        ↓
Selenium + Chrome WebDriver
        ↓
Movie Data Extraction
        ↓
Data Cleaning & Processing
        ↓
Pandas DataFrame
        ↓
movies.csv
        ↓
Web Dashboard
