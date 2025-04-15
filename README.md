# Iranian Stock Market Sentiment Analysis

## Project Overview
This project aims to analyze and predict investor sentiment in the Iranian stock market using Persian-language content from various sources. The goal is to create a tool that can help reduce emotional decision-making among retail investors by providing data-driven insights.

## Project Structure
```
iranian-stock-sentiment-analysis/
├── data/               # Data storage
│   ├── raw/           # Raw scraped data
│   └── processed/     # Processed and cleaned data
├── docs/              # Documentation
│   ├── api/          # API documentation
│   └── reports/      # Analysis reports
├── notebooks/         # Jupyter notebooks for analysis
├── src/              # Source code
│   ├── data/        # Data collection and processing
│   ├── models/      # Machine learning models
│   ├── utils/       # Utility functions
│   └── api/         # API endpoints
└── tests/            # Unit tests
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/iranian-stock-sentiment-analysis.git
cd iranian-stock-sentiment-analysis
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Components

### 1. Data Collection
- Web scraping of Persian financial forums
- Telegram channel data collection
- Financial news aggregation

### 2. Text Processing
- Persian text preprocessing using Hazm
- Sentiment analysis
- Feature extraction

### 3. Machine Learning Models
- Logistic Regression
- Support Vector Machine (SVM)
- XGBoost
- Deep Learning models (optional)

### 4. API Development
- RESTful API for model predictions
- Data visualization endpoints

## Development Workflow

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Description of your changes"
```

3. Push your changes and create a pull request:
```bash
git push origin feature/your-feature-name
```

## Contributing
Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Hazm library for Persian text processing
- Various open-source machine learning libraries
- Contributors and maintainers 