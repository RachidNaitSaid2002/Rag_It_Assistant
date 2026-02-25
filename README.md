# Racg_It_Assistant

A powerful RAG (Retrieval-Augmented Generation) IT Assistant that transforms your documentation into an intelligent Q&A system.

## Features

- **PDF Document Processing** - Upload and process PDF documents with intelligent text extraction
- **Smart Text Chunking** - Automatic document splitting with overlap for optimal context preservation
- **Vector Semantic Search** - BAAI/bge-m3 multilingual embeddings for accurate semantic matching
- **ChromaDB Vector Store** - Fast and efficient similarity search
- **Google Gemini 2.5 Flash** - State-of-the-art LLM for natural language responses
- **REST API (FastAPI)** - Fast, secure, and production-ready endpoints
- **User Authentication** - JWT-based authentication system
- **Query History** - Track and manage all queries
- **Answer Validation** - Built-in answer quality checking
- **Question Clustering** - ML-powered question categorization
- **MLflow Tracking** - Full observability of API performance and metrics

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   PDF Docs  │────▶│  Processing  │────▶│   ChromaDB     │
└─────────────┘     └──────────────┘     │  (Vector Store) │
                                          └────────┬────────┘
                                                   │
                                                   ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   User      │────▶│  FastAPI     │◀────│  RetrievalQA    │
│  (Query)    │     │   Backend    │     │   + Gemini LLM  │
└─────────────┘     └──────────────┘     └─────────────────┘
```

## Tech Stack

- **Backend**: FastAPI (Python)
- **LLM**: Google Gemini 2.5 Flash
- **Embeddings**: BAAI/bge-m3
- **Vector Store**: ChromaDB
- **Database**: SQLAlchemy (SQLite)
- **Auth**: JWT (Python-Jose)
- **ML Tracking**: MLflow
- **PDF Processing**: PyPDFLoader

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Rag_It_Assistant
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key_here
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

6. Access API docs at: `http://localhost:8000/docs`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/auth/register` | POST | Register new user |
| `/auth/login` | POST | User login |
| `/query/query` | POST | Ask a question |
| `/history` | GET | Get query history |

## Usage

### Register a User
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "email": "user@example.com", "password": "password123"}'
```

### Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"
```

### Ask a Question
```bash
curl -X POST "http://localhost:8000/query/query?question=How do I configure VPN?" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Project Structure

```
Rag_It_Assistant/
├── app/
│   ├── auth/           # JWT authentication
│   ├── core/           # Configuration
│   ├── db/             # Database connection
│   ├── models/         # SQLAlchemy models
│   ├── routes/         # API routes
│   ├── schemas/        # Pydantic schemas
│   ├── utils/          # Utility functions
│   └── main.py         # FastAPI app
├── scripts/            # Core RAG processing
│   ├── Chunking.py
│   ├── Core_function.py
│   ├── Embedding_Chunkes.py
│   ├── LoadPDF.py
│   ├── Model.py
│   ├── Pre_Prompt.py
│   ├── Retrieve_Data.py
│   └── RetrievalQA.py
├── README.md
└── requirements.txt
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Google Gemini API key |
| `SECRET_KEY` | JWT secret key |
| `ALGORITHM` | JWT algorithm (default: HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time |

## License

MIT License
