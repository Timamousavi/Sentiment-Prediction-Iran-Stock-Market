# Iranian Stock Market Sentiment Analysis - User Guide

## Introduction
This guide will help you get started with using the Iranian Stock Market Sentiment Analysis system. The system provides sentiment analysis for Persian financial text, helping you understand market sentiment from various sources.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Basic Usage](#basic-usage)
3. [Advanced Features](#advanced-features)
4. [Best Practices](#best-practices)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection

### Installation
1. Clone the repository:
```bash
git clone https://github.com/your-repo/iranian-stock-sentiment-analysis.git
cd iranian-stock-sentiment-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with:
```
API_KEY=your_api_key_here
MODEL_PATH=models/v1
```

## Basic Usage

### Single Text Analysis
```python
from src.models.sentiment_analyzer import SentimentAnalyzer

# Initialize analyzer
analyzer = SentimentAnalyzer()

# Analyze text
text = "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد"
labels, probabilities = analyzer.predict([text])

# Get sentiment and confidence
sentiment = "positive" if labels[0] == 1 else "negative"
confidence = probabilities[0][1] if labels[0] == 1 else probabilities[0][0]

print(f"Sentiment: {sentiment}")
print(f"Confidence: {confidence:.2f}")
```

### Batch Analysis
```python
# Analyze multiple texts
texts = [
    "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد",
    "بازار بورس امروز با کاهش شاخص همراه بود"
]
labels, probabilities = analyzer.predict(texts)

for i, (label, prob) in enumerate(zip(labels, probabilities)):
    sentiment = "positive" if label == 1 else "negative"
    confidence = prob[1] if label == 1 else prob[0]
    print(f"Text {i+1}: {sentiment} (confidence: {confidence:.2f})")
```

## Advanced Features

### Model Training
```python
# Prepare training data
texts = [
    "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد",
    "بازار بورس امروز با کاهش شاخص همراه بود"
]
labels = [1, 0]  # 1: positive, 0: negative

# Train model
metrics = analyzer.train(texts, labels)
print("Training metrics:", metrics)
```

### Hyperparameter Tuning
```python
# Tune model parameters
best_params = analyzer.tune_hyperparameters(texts, labels)
print("Best parameters:", best_params)
```

### Model Versioning
```python
# Save model
analyzer.save_model("models/v1")

# Load model
new_analyzer = SentimentAnalyzer("models/v1")
```

## Best Practices

### Text Preparation
1. Remove URLs and special characters
2. Normalize Persian text
3. Handle financial terms properly
4. Consider text length (optimal: 50-500 characters)

### Performance Optimization
1. Use batch processing for multiple texts
2. Cache frequently used models
3. Monitor processing time
4. Use appropriate model version

### Error Handling
```python
try:
    result = analyzer.predict(text)
except Exception as e:
    print(f"Error: {str(e)}")
    # Handle error appropriately
```

## Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Check model path
   - Verify model files exist
   - Ensure correct permissions

2. **Text Processing Error**
   - Check text encoding
   - Verify text format
   - Ensure proper Persian text

3. **Performance Issues**
   - Monitor memory usage
   - Check processing time
   - Optimize batch size

### Debugging
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Test with sample text
analyzer.predict(["سهام فولاد"])
```

## FAQ

### Q: What types of text work best?
A: The system works best with:
- Financial news articles
- Stock market reports
- Company announcements
- Market analysis

### Q: How accurate is the sentiment analysis?
A: Accuracy depends on:
- Text quality and relevance
- Model version and training data
- Text length and complexity

### Q: Can I use the system for other languages?
A: The system is specifically designed for Persian financial text. Using it for other languages or domains may yield poor results.

### Q: How do I improve results?
A: To improve results:
1. Use clear, relevant financial text
2. Ensure proper text normalization
3. Use appropriate model version
4. Consider retraining with domain-specific data

### Q: What's the maximum text length?
A: The system can handle texts up to 1000 characters, but optimal performance is achieved with 50-500 characters.

## Support
For additional support:
- Check the [API Documentation](API.md)
- Visit the [GitHub repository](https://github.com/your-repo)
- Contact support@example.com 