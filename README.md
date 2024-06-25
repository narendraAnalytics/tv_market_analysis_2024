
# Tv_Market_analysis_2024

![Data Cleaning Process](docs/images/Image_Robts_tv.webp)


## Project Description
Tv_Market_analysis_2024 is a comprehensive data analysis project focused on the television market. This project aims to analyze market trends, sales data, and consumer preferences to provide valuable insights into the TV industry's current and future landscape. By leveraging various data analysis techniques and visualization tools, the project will explore key factors influencing the market, including pricing, brand performance, technological advancements, and regional demand variations. The analysis will help stakeholders make informed decisions and identify growth opportunities within the TV market in 2024.

## Dataset

The dataset contains information about various TVs in the market, including their specifications, prices, and other relevant details. The data has been collected from multiple sources and consolidated into a single dataset.

# TV Data Scraper

This Python script uses Selenium to scrape TV data from 91mobiles.com. It extracts information such as name, price, display, features, connectivity, and design from all available pages and saves the data to a CSV file.

## Requirements

- Python 3.x
- Pandas
- Selenium
- Chrome WebDriver

## Installation

1. Install Python packages:
    ```sh
    pip install pandas selenium
    ```

2. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system's PATH or specify its location in the script.

## Usage

1. Clone this repository or copy the script to your local machine.
2. Ensure Chrome WebDriver is correctly installed and accessible.
3. Run the script:

    ```sh
    python tv_scraper.py
    ```


## Data Cleaning and Preprocessing

Data cleaning and preprocessing have been performed using SQL queries to ensure the dataset is ready for analysis. The following steps were taken:

1. **Handling Missing Values:**
   - Missing values in important columns were imputed with appropriate values.
   - Rows with a high percentage of missing data were removed.

2. **Data Transformation:**
   - Relevant columns were transformed to appropriate data types for analysis.


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for tv_market_analysis
│                         and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── tv_market_analysis                <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes tv_market_analysis a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
```

--------

