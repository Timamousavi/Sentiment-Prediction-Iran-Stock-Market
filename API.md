# Iranian Stock Market Sentiment Analysis API Documentation

## Overview
This API provides sentiment analysis for Persian financial text, specifically focused on the Iranian stock market. It uses machine learning models to analyze text and determine sentiment (positive/negative) with confidence scores.

## Authentication
All endpoints except `/token` require authentication using JWT tokens.

### Get Access Token
```http
POST /token
Content-Type: application/x-www-form-urlencoded

username=testuser&password=testpass
```

Response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

Use the `access_token` in the Authorization header for subsequent requests:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

## Endpoints

### Analyze Single Text
```http
POST /analyze
Authorization: Bearer <token>
Content-Type: application/json

{
    "text": "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد",
    "model_version": "latest"
}
```

Response:
```json
{
    "sentiment": "positive",
    "confidence": 0.85,
    "model_version": "1.0.0",
    "processing_time": 0.12
}
```

### Analyze Multiple Texts
```http
POST /analyze/batch
Authorization: Bearer <token>
Content-Type: application/json

{
    "texts": [
        "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد",
        "بازار بورس امروز با کاهش شاخص همراه بود"
    ],
    "model_version": "latest"
}
```

Response:
```json
{
    "results": [
        {
            "sentiment": "positive",
            "confidence": 0.85,
            "model_version": "1.0.0",
            "processing_time": 0.0
        },
        {
            "sentiment": "negative",
            "confidence": 0.78,
            "model_version": "1.0.0",
            "processing_time": 0.0
        }
    ],
    "total_processing_time": 0.15
}
```

### Get Model Information
```http
GET /model/info
Authorization: Bearer <token>
```

Response:
```json
{
    "version": "1.0.0",
    "created_at": "2024-01-01T00:00:00",
    "last_updated": "2024-01-01T00:00:00",
    "performance_metrics": {
        "train": {
            "accuracy": 0.92,
            "precision": 0.91,
            "recall": 0.93,
            "f1": 0.92
        },
        "test": {
            "accuracy": 0.89,
            "precision": 0.88,
            "recall": 0.90,
            "f1": 0.89
        }
    }
}
```

## Rate Limiting
The API implements rate limiting to prevent abuse:
- Root endpoint: 5 requests per minute
- Analysis endpoints: 10 requests per minute
- Model info endpoint: 5 requests per minute

When rate limit is exceeded, the API returns a 429 status code.

## Error Handling
The API returns appropriate HTTP status codes and error messages:

- 400: Bad Request
- 401: Unauthorized
- 422: Validation Error
- 429: Too Many Requests
- 500: Internal Server Error

Example error response:
```json
{
    "detail": "Error message here"
}
```

## Input Validation
- Text length: 1-1000 characters
- Batch size: 1-100 texts
- Model version: Must be a valid version string

## Security
- All endpoints require authentication
- JWT tokens expire after 30 minutes
- HTTPS is required for all requests
- Rate limiting prevents abuse

## Best Practices
1. Always use HTTPS
2. Store tokens securely
3. Implement proper error handling
4. Respect rate limits
5. Use batch endpoints for multiple texts
6. Check model version compatibility

## Example Usage

### Python
```python
import requests

# Get token
response = requests.post(
    "https://api.example.com/token",
    data={"username": "testuser", "password": "testpass"}
)
token = response.json()["access_token"]

# Analyze text
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(
    "https://api.example.com/analyze",
    json={"text": "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد"},
    headers=headers
)
result = response.json()
print(f"Sentiment: {result['sentiment']}, Confidence: {result['confidence']}")
```

### JavaScript
```javascript
// Get token
const response = await fetch('https://api.example.com/token', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'username=testuser&password=testpass'
});
const { access_token } = await response.json();

// Analyze text
const result = await fetch('https://api.example.com/analyze', {
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${access_token}`,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        text: 'سهام شرکت فولاد امروز با افزایش قیمت مواجه شد'
    })
});
const data = await result.json();
console.log(`Sentiment: ${data.sentiment}, Confidence: ${data.confidence}`);
```

## Support
For support, please contact:
- Email: support@example.com
- GitHub Issues: https://github.com/your-repo/issues 