# PamBot

PamBot is a conversational AI chatbot built with **FastAPI** and **RAG (Retrieval-Augmented Generation)** that answers questions about personal information and projects. It uses vector embeddings and semantic search to provide accurate, context-aware responses.

## 🎯 Features

- **Intelligent Q&A**: Ask questions about Pam's information and projects
- **RAG Architecture**: Combines retrieval-augmented generation for accurate answers
- **Vector Search**: Uses Qdrant vector database for efficient semantic search
- **REST API**: FastAPI-based API with health check and chat endpoints
- **Extensible Design**: Easy to add new information and customize responses

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Vector Database**: [Qdrant](https://qdrant.tech/)
- **API Server**: Uvicorn
- **Configuration**: python-dotenv, Pydantic Settings
- **HTTP Client**: httpx
- **Language Model**: External LLM API (configurable)
- **Embeddings**: External embedding API (configurable)

## 📁 Project Structure

```
PamBot/
├── app/
│   ├── config.py                 # Configuration settings
│   ├── main.py                   # FastAPI application entry point
│   ├── routes/
│   │   └── pambot.py            # API route handlers
│   ├── schemas/
│   │   └── pambot_schema.py      # Request/response data models
│   ├── services/
│   │   ├── embedding_service.py  # Text embedding generation
│   │   ├── llm_service.py        # Language model interactions
│   │   └── rag_service.py        # RAG orchestration
│   ├── utils/
│   │   ├── prompt_builder.py     # Prompt construction utilities
│   │   ├── split_text.py         # Text chunking/splitting
│   │   └── textloader.py         # Document loading
│   └── vectorstore/
│       └── qdrant.py             # Qdrant vector store client
├── data/
│   └── personal_data.md          # Source data about Pam
├── script/
│   └── ingest_personal_info.py   # Data ingestion script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Qdrant instance (local or cloud)
- External API access for embeddings and LLM

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd PamBot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the root directory:

   ```env
   # Qdrant Configuration
   QDRANT_URL=http://localhost:6333
   QDRANT_API_KEY=your_api_key_here
   QDRANT_COLLECTION_NAME=pambot_personal_info

   # Embedding API Configuration
   EMBEDDING_API_URL=https://your-embedding-api.com
   EMBEDDING_API_KEY=your_embedding_key_here

   # LLM API Configuration
   LLM_API_URL=https://your-llm-api.com
   LLM_API_KEY=your_llm_key_here
   LLM_MODEL_NAME=your_model_name
   ```

### Data Ingestion

To ingest personal data into the vector database:

```bash
python script/ingest_personal_info.py
```

This script will:

1. Read data from `data/personal_data.md`
2. Split text into chunks
3. Generate embeddings
4. Store in Qdrant vector database

## 📡 API Documentation

### Root Endpoint

- **GET** `/`
  - Returns: Welcome message

### Health Check

- **GET** `/health`
  - Returns: `{"status": "ok"}`

### Ask Question

- **POST** `/pambot/ask`
  - Request body:
    ```json
    {
      "question": "Tell me about Pam"
    }
    ```
  - Response:
    ```json
    {
      "question": "Tell me about Pam",
      "answer": "Pam is...",
      "sources": ["document1", "document2"]
    }
    ```

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🏃 Running the Application

### Development Mode

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🔧 Configuration Details

### Services

#### Embedding Service (`app/services/embedding_service.py`)

- Generates vector embeddings for text
- Communicates with external embedding API
- Handles embedding caching

#### LLM Service (`app/services/llm_service.py`)

- Handles interactions with large language models
- Manages API calls to external LLM providers
- Processes model responses

#### RAG Service (`app/services/rag_service.py`)

- Orchestrates the retrieval-augmented generation pipeline
- Retrieves relevant documents from vector database
- Generates answers using LLM with retrieved context

#### Vector Store (`app/vectorstore/qdrant.py`)

- Manages Qdrant vector database connections
- Performs semantic similarity search
- Handles vector storage and retrieval

## 📝 Data Format

Personal data should be stored in `data/personal_data.md` in Markdown format:

```markdown
# Pam's Information

## About Pam

- Name: Pam
- Profession: Software Engineer
- Location: ...

## Projects

### Project 1

Description and details...

### Project 2

Description and details...
```

## 🐛 Troubleshooting

### Common Issues

1. **Qdrant Connection Error**
   - Ensure Qdrant is running and accessible
   - Check `QDRANT_URL` in `.env`

2. **Embedding API Timeout (504 Gateway Time-out)**
   - This is a known issue with external model endpoints
   - Retry the request after a delay
   - Consider using a fallback provider

3. **Collection Not Found**
   - Run `ingest_personal_info.py` to create and populate the collection
   - Verify collection name in `.env`

## 📚 Development

### Running Tests

```bash
pytest tests/
```

### Code Structure Tips

- Services are in `app/services/` - modify here for business logic
- Routes are in `app/routes/` - modify here for API endpoints
- Schemas define request/response formats
- Utils contain helper functions for text processing

## 📄 License

[Add your license information here]

## 👤 Author

PamBot is maintained by Pam and contributors.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
