# ScrapeThisSite Scraper

Hey there! This is a practice project which uses Scrapy to grab data from the website [ScrapeThisSite.com](https://scrapethissite.com/).


## Target Website

* **URL:** `https://scrapethissite.com/`
* **Purpose:** A place to practice and learn web scraping.

## Main Spiders

This project includes spiders for different parts of the site:

* `hockey_teams`: Grabs hockey team info from the forms and paginated section (`.../pages/forms/`).
* `countries`: Extracts country data from the simple section (`.../pages/simple/`).
* `oscar_films`: Collects Oscar-winning film info from the section loaded with AJAX (`.../pages/ajax-javascript/`).
* *(Feel free to add more spiders!)*

## What You'll Need

* Python 3.8+
* Scrapy

## How to Install It

1.  **Clone it:**
    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```
2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # Activate on Linux/macOS:
    source venv/bin/activate
    # Activate on Windows:
    .\venv\Scripts\activate
    ```
3.  **Install packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, just run `pip install Scrapy`)*

## How to Run It

To run a spider and save its data, use this command in your terminal:

```bash
scrapy crawl <spider_name> -O <output_filename>