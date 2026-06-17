# Personal Information

## Basic Information

Name: Phạm Tuấn Anh
Nickname: Pam
Brand name: AhhPam
Work email: [ahhpam.work@gmail.com](mailto:ahhpam.work@gmail.com)
GitHub: https://github.com/Anhhphamne25

Phạm Tuấn Anh, also known as Pam, is an Information Technology student interested in backend development, artificial intelligence, RAG systems, vector databases, and practical software products.

He is currently studying Information Technology at the College of Technology, National Economics University.

Pam uses the personal brand name AhhPam for portfolio, GitHub projects, and personal AI-related products.

## Career Goal

Phạm Tuấn Anh aims to become a Backend Developer or AI Engineer.

He is especially interested in building backend systems that can connect with AI models, process data, retrieve knowledge from vector databases, and provide practical AI-powered features for real users.

His long-term direction is to work on AI backend systems, RAG applications, agent-based systems, and intelligent automation tools.

## Technical Skills

### Programming Languages

- Python
- JavaScript
- TypeScript

### Backend Development

- FastAPI
- NestJS
- ExpressJS
- REST API development
- API integration
- Authentication and authorization basics
- JWT
- RBAC
- Server-side application design

### AI Engineering

- Retrieval-Augmented Generation
- Embedding models
- Vector search
- Prompt engineering
- Multi-agent workflow
- AI API integration
- LLM-based application development
- Context retrieval and answer generation

### Vector Database

- Qdrant
- Collection design
- Chunk storage
- Vector search
- Payload filtering
- Session-based vector retrieval

### Database

- PostgreSQL
- MongoDB
- Prisma ORM
- Basic database design

### Frontend

- React
- Next.js
- Tailwind CSS
- Building interfaces that connect with backend APIs

### Tools and Workflow

- Git
- GitHub
- Docker basics
- API testing
- Environment configuration
- Project documentation

## Main Interests

Phạm Tuấn Anh is interested in:

- Playing games
- Listening to music
- Watching movies
- Building tools and systems that serve his own learning, work, and productivity
- Creating practical AI products
- Learning backend and AI engineering through real projects

He enjoys creating personal tools that solve real problems instead of only building demo applications.

## Achievements

### 2023 - Student of Five Merits at University Level

Phạm Tuấn Anh received the “Student of Five Merits” title at university level in 2023.

This title recognizes students who satisfy five important criteria, including academic performance, ethics, physical fitness, volunteering, and integration.

### 2025 - Olympic Informatics Award

Phạm Tuấn Anh received an award in the university-level Olympic Informatics competition in 2025.

This competition focused on informatics and programming ability at the university level.

### 2026 - First Prize in University-Level Scientific Research

Phạm Tuấn Anh won First Prize in university-level scientific research in 2026.

Research topic:
“Building a Data Lake model for a RAG system with knowledge gap detection in searching and analyzing academic papers at National Economics University.”

The project achieved the highest score at the university level, ranked number one, and was selected to compete at the Ministry of Education and Training level.

### TODO - Additional Achievement

Add one more achievement here if needed.

## Experience

### Frontend Developer - Course 2.0 NEU Project

Phạm Tuấn Anh worked on the frontend of the Course 2.0 NEU project.

The system was designed to support the management, processing, and storage of training-related procedures for the training management department.

His work focused on building the user interface, handling raw data display, and connecting frontend components with backend APIs.

The system was deployed and used in practice.

### AI RAG Research System

Phạm Tuấn Anh worked on an AI RAG system designed to support scientific research.

The system uses Retrieval-Augmented Generation to search, retrieve, analyze, and answer questions based on academic documents and research papers.

The project involved document processing, embedding generation, vector storage, context retrieval, and answer generation using AI models.

### AI-Based Learning and Grading Systems

Phạm Tuấn Anh has experience building AI-supported systems for education, including exercise generation and answer grading.

These systems use AI models through server-hosted APIs and combine backend logic with structured prompts, rules, and retrieval mechanisms to improve output quality.

## Projects

### PamBot - Personalized AI Assistant

PamBot is a personalized AI assistant built with FastAPI, Qdrant, embedding models, and a server-hosted Qwen AI model.

The main idea of PamBot is simple:

1. Prepare a personal information file.
2. Split the file into chunks.
3. Convert chunks into embeddings.
4. Store the vectors and payloads in Qdrant.
5. Receive a user question through an API endpoint.
6. Convert the question into an embedding.
7. Retrieve the most relevant chunks from Qdrant.
8. Send the retrieved context to the AI model.
9. Return a personalized answer.

PamBot exposes a simple backend endpoint:

POST /v1/pambot

The project does not focus on complex user management or frontend features. Instead, it focuses on building a clean and practical RAG backend for personal information retrieval.

The AI model used in PamBot is Qwen 8B, hosted on a server and connected through an internal API.

Key technologies:

- FastAPI
- Qdrant
- Python
- Embedding API
- Qwen 8B
- RAG pipeline
- Markdown-based personal data

### Exercise Generation System

This project is an AI-powered exercise generation system.

The system uses a multi-agent workflow and loop-based processing to generate learning exercises.

Instead of only calling an AI model once, the system divides the task into smaller steps and lets different AI agents handle different responsibilities.

The AI connection method is similar to PamBot. The AI model is hosted on a server and accessed through an API.

Key ideas:

- Multi-agent workflow
- Loop-based generation
- AI-generated exercises
- Backend-controlled AI pipeline
- Structured prompt design

### AI Grading System

This project is an AI-based grading system.

The system is designed to grade student answers or programming submissions based on a defined rule set.

Instead of letting the AI judge freely, the system creates multiple processing nodes to compare, verify, and enrich the information before producing the final grading result.

The goal is to make AI grading more consistent, explainable, and aligned with predefined grading rules.

Key ideas:

- Rule-based grading support
- AI-assisted evaluation
- Multiple processing nodes
- Comparison and verification
- Context enrichment
- More reliable AI scoring

### QA Docs - Document Question Answering System

QA Docs is a document-based question answering system using RAG.

The frontend creates a session ID and sends it to the backend. The backend processes uploaded documents, creates embeddings, and stores them in Qdrant together with the session ID.

When the user asks a question, the system retrieves only the chunks that belong to the current session and uses them as context for the AI model.

To avoid filling up vector storage, the system automatically deletes temporary session data after a certain period of time.

Main workflow:

1. Frontend creates a session ID.
2. User uploads documents.
3. Backend extracts and processes text.
4. Text is split into chunks.
5. Chunks are converted into embeddings.
6. Vectors are stored in Qdrant with the session ID.
7. User asks a question.
8. Backend retrieves relevant chunks using vector search and session filtering.
9. AI generates an answer based on the retrieved context.
10. Temporary data is deleted after a defined time.

Key technologies:

- FastAPI or backend API service
- Qdrant
- Embedding model
- Session-based RAG
- Automatic cleanup mechanism
- Document question answering

## Research Interests

Phạm Tuấn Anh is interested in:

- Retrieval-Augmented Generation
- AI Backend Engineering
- Vector databases
- Data Lake architecture
- Knowledge gap detection
- Academic paper analysis
- AI systems for education
- Multi-agent AI systems
- LLM-based automation
- Practical AI applications

## Working Style

Phạm Tuấn Anh prefers building projects by starting from a simple working MVP first, then improving the structure and features later.

He values practical implementation over unnecessary complexity.

When building backend or AI systems, he prefers:

- Simple architecture
- Clear API flow
- Small working modules
- Easy-to-debug code
- Real use cases
- Clean but not over-engineered folder structure

## Communication Style

Phạm Tuấn Anh prefers explanations that are:

- Practical
- Direct
- Easy to understand
- Not too academic
- Not overcomplicated
- Supported by concrete examples
- Written in Vietnamese by default

He likes technical explanations that show how a system actually works instead of only explaining abstract theory.
