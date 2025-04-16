# 📈 Iranian Stock Market Sentiment Analysis

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/iranian-stock-sentiment/badge/?version=latest)](https://iranian-stock-sentiment.readthedocs.io/en/latest/?badge=latest)

</div>

## 🌟 Overview

This project aims to revolutionize investment decision-making in the Iranian stock market by leveraging advanced natural language processing and machine learning techniques. By analyzing Persian-language content from various financial sources, we provide data-driven insights to help investors make more informed decisions.

<div align="center">
  <img src="docs/images/sentiment-analysis.png" alt="Sentiment Analysis Flow" width="600"/>
</div>

## 🚀 Features

- **Advanced Text Processing**
  - Persian text normalization and tokenization
  - Financial term extraction
  - Sentiment analysis
  - Custom stopword handling

- **Multiple Data Sources**
  - Financial forums
  - Telegram channels
  - News articles
  - Social media

- **Machine Learning Models**
  - Logistic Regression
  - Support Vector Machines
  - Random Forest
  - Deep Learning (optional)

- **RESTful API**
  - Real-time sentiment analysis
  - Batch processing
  - Detailed analysis reports

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/iranian-stock-sentiment-analysis.git
   cd iranian-stock-sentiment-analysis
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

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

## 🧪 Usage

### Data Collection
```python
from src.data.scraper import FinancialContentScraper

scraper = FinancialContentScraper("https://example-forum.com")
posts = scraper.scrape_forum(page_count=2)
```

### Text Processing
```python
from src.utils.text_processor import PersianTextProcessor

processor = PersianTextProcessor()
processed = processor.process_text("سهام شرکت فولاد امروز با افزایش قیمت مواجه شد")
```

### Sentiment Analysis
```python
from src.models.sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()
results = analyzer.train(texts, labels)
prediction = analyzer.predict("سهام شرکت فولاد امروز با افزایش قیمت مواجه شد")
```

### API Usage
```bash
# Start the API server
uvicorn src.api.app:app --reload

# Make a request
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد"}'
```

## 📊 Results

<div align="center">
  <img src="docs/images/results.png" alt="Analysis Results" width="800"/>
</div>

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](docs/CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hazm](https://github.com/sobhe/hazm) - Persian text processing library
- [Scikit-learn](https://scikit-learn.org/) - Machine learning library
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- All contributors and maintainers

## 📞 Contact

For questions or suggestions, please open an issue or contact us at [fatemehmousavy@ut.ac.ir](mailto:fatemehmousavy@ut.ac.ir).

---

<div align="center">
  <sub>Built with ❤️ by Tima Mousavi</sub>
</div> 
