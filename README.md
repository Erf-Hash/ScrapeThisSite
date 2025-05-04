# ScrapeThisSite Scraper

Hey there! This is a practice project which uses Scrapy to grab data from the website [ScrapeThisSite.com](https://scrapethissite.com/).


## Target Website

* **URL:** `https://scrapethissite.com/`
* **Purpose:** A place to practice and learn web scraping.


## Requirements

* Python 3.8+
* Scrapy

## How to Install It

1.  **Clone it:**
    ```bash
    git clone [<your-repository-url>](https://github.com/Erf-Hash/ScrapeThisSite)
    cd ScrapeThisSite
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

## How to Run It

To run a spider and save its data, use this command in your terminal:

```bash
scrapy crawl oscar -O <output_filename>