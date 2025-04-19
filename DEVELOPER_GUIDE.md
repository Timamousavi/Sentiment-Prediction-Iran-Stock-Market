# Iranian Stock Market Sentiment Analysis - Developer Guide

## Introduction
This guide is intended for developers who want to contribute to or extend the Iranian Stock Market Sentiment Analysis system. It covers the architecture, development workflow, and best practices.

## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Development Setup](#development-setup)
3. [Code Structure](#code-structure)
4. [Adding New Features](#adding-new-features)
5. [Testing](#testing)
6. [Documentation](#documentation)
7. [Deployment](#deployment)
8. [Contributing](#contributing)

## Architecture Overview

### System Components
1. **Text Processing**
   - Persian text normalization
   - Financial term extraction
   - Stopword removal
   - Tokenization

2. **Machine Learning**
   - Feature extraction
   - Model training
   - Prediction
   - Model versioning

3. **API Layer**
   - FastAPI application
   - Authentication
   - Rate limiting
   - Error handling

### Data Flow
```
Input Text → Text Processing → Feature Extraction → Model Prediction → API Response
```

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment
- Docker (optional)

### Setup Steps
1. Clone the repository:
```bash
git clone https://github.com/your-repo/iranian-stock-sentiment-analysis.git
cd iranian-stock-sentiment-analysis
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Set up pre-commit hooks:
```bash
pre-commit install
```

## Code Structure

```
src/
├── api/
│   ├── main.py           # FastAPI application
│   └── routes/           # API endpoints
├── models/
│   ├── sentiment_analyzer.py
│   └── model_utils.py
├── utils/
│   ├── text_processor.py
│   └── data_utils.py
└── tests/
    ├── test_sentiment_analyzer.py
    ├── test_api.py
    └── test_integration.py
```

### Key Components

1. **Text Processor**
```python
class FinancialTextProcessor:
    def normalize_text(self, text: str) -> str:
        # Normalize Persian text
        pass

    def extract_financial_terms(self, text: str) -> List[str]:
        # Extract financial terms
        pass
```

2. **Sentiment Analyzer**
```python
class SentimentAnalyzer:
    def train(self, texts: List[str], labels: List[int]) -> Dict:
        # Train model
        pass

    def predict(self, texts: List[str]) -> Tuple[np.ndarray, np.ndarray]:
        # Make predictions
        pass
```

3. **API Endpoints**
```python
@app.post("/analyze")
async def analyze_sentiment(request: SentimentRequest):
    # Handle sentiment analysis request
    pass
```

## Adding New Features

### 1. Text Processing
To add new text processing features:
1. Extend `FinancialTextProcessor` class
2. Add unit tests
3. Update documentation

Example:
```python
def add_special_characters(self, text: str) -> str:
    # Add new text processing method
    pass
```

### 2. Model Improvements
To improve the model:
1. Modify feature extraction
2. Update model architecture
3. Add new evaluation metrics

Example:
```python
def extract_advanced_features(self, text: str) -> Dict:
    # Add new feature extraction
    pass
```

### 3. API Endpoints
To add new API endpoints:
1. Create new route
2. Add request/response models
3. Implement error handling

Example:
```python
@app.post("/analyze/advanced")
async def advanced_analysis(request: AdvancedRequest):
    # Implement new endpoint
    pass
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_sentiment_analyzer.py

# Run with coverage
pytest --cov=src
```

### Writing Tests
1. Unit Tests
```python
def test_text_processing():
    processor = FinancialTextProcessor()
    result = processor.normalize_text("سهام فولاد")
    assert isinstance(result, str)
```

2. Integration Tests
```python
def test_end_to_end_workflow():
    # Test complete workflow
    pass
```

3. API Tests
```python
def test_api_endpoint():
    response = client.post("/analyze", json={"text": "سهام فولاد"})
    assert response.status_code == 200
```

## Documentation

### Code Documentation
- Use docstrings for all functions and classes
- Follow Google style guide
- Include type hints

Example:
```python
def process_text(self, text: str) -> Dict[str, Any]:
    """Process text and extract features.
    
    Args:
        text: Input text to process
        
    Returns:
        Dictionary containing processed features
    """
    pass
```

### API Documentation
- Update OpenAPI schema
- Add example requests/responses
- Document error codes

### User Documentation
- Update user guide
- Add examples
- Document new features

## Deployment

### Local Deployment
1. Build Docker image:
```bash
docker build -t sentiment-analysis .
```

2. Run container:
```bash
docker run -p 8000:8000 sentiment-analysis
```

### Production Deployment
1. Set up environment variables
2. Configure logging
3. Enable monitoring
4. Set up CI/CD pipeline

## Contributing

### Workflow
1. Fork repository
2. Create feature branch
3. Make changes
4. Run tests
5. Submit pull request

### Code Style
- Follow PEP 8
- Use type hints
- Write docstrings
- Add tests

### Pull Request Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Code style checked
- [ ] All tests pass
- [ ] No merge conflicts

## Support
For development support:
- Check GitHub issues
- Join developer chat
- Contact maintainers 