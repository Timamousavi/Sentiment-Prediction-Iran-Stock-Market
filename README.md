# Iranian Stock Market Sentiment Analysis

This project aims to predict investor sentiment in the Iranian stock market using behavioral data and machine learning techniques.

## Project Overview

The project analyzes Persian-language behavioral data from multiple sources to predict market sentiment:
- Stock forums (e.g., boursy.com)
- Telegram channels
- Financial news headlines

## Project Structure

```
iranian_market_sentiment/
├── data/
│   ├── raw/                # Raw scraped data
│   └── processed/          # Cleaned and processed datasets
├── src/
│   ├── data_collection/    # Web scraping and data gathering scripts
│   ├── preprocessing/      # Text processing and feature extraction
│   ├── models/            # ML model implementations
│   └── evaluation/        # Model evaluation and metrics
├── notebooks/             # Jupyter notebooks for analysis
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Data Collection

The project collects data from three main sources:
1. Iranian stock forums
2. Telegram channels
3. Financial news sources

Data collection respects ethical guidelines and website terms of service.

## Features

- Persian text preprocessing using Hazm library
- Custom financial sentiment lexicon
- Multiple ML models (Logistic Regression, SVM, XGBoost)
- Evaluation metrics (Accuracy, Precision, Recall)

## Usage

1. Data Collection:
```bash
python src/data_collection/scraper.py
```

2. Text Preprocessing:
```bash
python src/preprocessing/process_text.py
```

3. Model Training:
```bash
python src/models/train.py
```


## Contributing

This is a research project. For collaboration inquiries, please contact me on fatemehmousavy@ut.ac.ir.


