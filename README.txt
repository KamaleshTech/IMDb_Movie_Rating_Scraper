# IMDb Movie Rating Scraper

A Python-based web scraping project that extracts movie information from the IMDb Top 250 Movies list using Selenium and Chrome WebDriver. The scraped data is stored in a CSV file and displayed through a simple web dashboard.

## Features

- Scrapes IMDb Top 250 movie data
- Extracts movie title
- Extracts release year
- Extracts IMDb rating
- Extracts movie ranking
- Stores data in CSV format
- Displays data in a simple web dashboard

## Technologies Used

- Python
- Selenium
- Pandas
- WebDriver Manager
- HTML
- CSS
- JavaScript

## Project Structure

```text
IMDb_Movie_Rating_Scraper/
│
├── scraper.py
├── movies.csv
├── app.py
├── requirements.txt
├── style.css
├── script.js
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd IMDb_Movie_Rating_Scraper
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Scraper

```bash
python scraper.py
```

### 4. Run the Web Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

## Output

The scraper generates a CSV file containing:

| Rank | Title | Year | Rating |
|------|--------|------|--------|
| 1 | The Shawshank Redemption | 1994 | 9.3 |
| 2 | The Godfather | 1972 | 9.2 |
| 3 | The Dark Knight | 2008 | 9.0 |

## Future Enhancements

- Export data to Excel format
- Add movie poster images
- Implement search and filter options
- Create interactive charts and visualizations
- Enable automatic data updates

## Author

**Kamalesh**