# 🎭 Sentiment Analysis API

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

A robust and scalable REST API for Spanish text sentiment analysis powered by FastAPI and the `pysentimiento` library. This service provides real-time sentiment classification (Positive/Negative/Neutral) with high accuracy and low latency.

## 🚀 Key Features

- **Spanish-Focused Analysis**: Specialized sentiment analysis for Spanish text
- **Multiple Input Methods**: Support for both GET and POST requests
- **Batch Processing**: Analyze multiple texts in a single request
- **Docker Support**: Easy deployment with containerization
- **High Performance**: Async processing for optimal response times
- **Production-Ready**: Comprehensive test suite and error handling

## 📋 Requirements

- Python 3.12 or higher
- Docker (optional)
- 2GB RAM minimum
- 1GB disk space

## 🛠️ Installation

### Local Setup

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/sentiment-analysis-api
    cd sentiment-analysis-api
    ```

2. Create and activate virtual environment
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    # OR
    source .venv/bin/activate  # Linux/macOS
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    # For development
    pip install -r requirements-dev.txt
    ```

### 🐋 Docker Setup

    ```bash
    docker build -t sentiment-api .
    docker run -d -p 8000:8000 sentiment-api
    ```

## 🚦 Quick Start

1. Start the server:
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

2. Access the API documentation:
    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc

## 🔌 API Reference

### Health Check
    ```http
    GET /health
    ```

### Single Text Analysis
    ```http
    GET /analyze?text=your_text_here
    ```

    ```http
    POST /analyze
    Content-Type: application/json

    {
        "text": "Me encanta este servicio"
    }
    ```

### Batch Analysis
    ```http
    POST /analyze_batch
    Content-Type: application/json

    {
        "texts": [
            "Primera frase para analizar",
            "Segunda frase para analizar"
        ]
    }
    ```

## 📊 Example Usage

### Using cURL
    ```bash
    curl -X POST "http://localhost:8000/analyze" \
         -H "Content-Type: application/json" \
         -d '{"text":"Me encanta este servicio"}'
    ```

### Using Python Client
    ```python
    from client import SentimentClient

    client = SentimentClient("http://localhost:8000")
    result = client.analyze("Me encanta este servicio")
    print(result)
    ```

## 🧪 Testing

Run the complete test suite:
    ```bash
    pytest tests/ -v --cov=app
    ```

Run specific test categories:
    ```bash
    pytest tests/test_api.py  # API tests only
    pytest tests/test_model.py  # Model tests only
    ```

## 📁 Project Structure

    ```
    sentiment-analysis-api/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── main.py          # FastAPI application and routes
    │   ├── model.py         # Sentiment analysis model
    │   └── utils.py         # Utility functions
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_api.py
    │   └── test_model.py
    │
    ├── Dockerfile
    ├── requirements.txt
    ├── requirements-dev.txt
    └── README.md
    ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/sentiment-analysis-api](https://github.com/yourusername/sentiment-analysis-api)

---

Made with ❤️ by maIQmej. 