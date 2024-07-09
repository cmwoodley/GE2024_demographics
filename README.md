# GE Demographics Data Dashboard

This project provides a data dashboard for visualizing election vote proportions against demographic information from constituencies in the UK. The demographic data is sourced from the Census 2021, utilizing post-2019 boundaries. Election results for GE2024 were scraped from the Sky News website using the code provided in the "web scraping" folder.

The dashboard is hosted at [ONS Dataset Portal](https://www.ons.gov.uk/datasets/create). It allows users to explore correlations between electoral outcomes and various demographic factors across constituencies.

## Features

- **Visualization of Election Vote Proportions**: Plot and analyze election vote proportions against demographic variables.
- **Interactive Dashboard**: Explore data through an interactive web interface.
- **Data Sources**:
  - Census 2021 demographic data
  - GE2024 election results from Sky News

## Requirements

The project requires Python 3.x and the dependencies listed in `requirements.txt`. Install the dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

To launch the dashboard, run the following command:

```
python ./app.py
```

This command starts the application and opens a local web server. You can access the dashboard by navigating to http://127.0.0.1:8050 in your web browser.


