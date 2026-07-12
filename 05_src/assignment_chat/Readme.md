# Athena AI Research Assistant

## Overview

Athena AI Research Assistant is a conversational AI application implemented using a Retrieval Augmented Generation (RAG) architecture.

The chatbot allows users to ask questions about a provided knowledge base. It retrieves relevant information from a vector database and uses a large language model to generate contextually relevant responses.

The application provides a simple conversational interface through Gradio.

---

## Features

The chatbot provides the following services:

- Conversational question answering
- Retrieval Augmented Generation (RAG)
- Document retrieval from a vector database
- Large language model response generation
- Conversation memory during a session
- Input and output validation through guardrails

---

## System Architecture

The application follows the pipeline:

User Input  
↓  
Gradio Interface  
↓  
Input Guardrails  
↓  
Conversation Memory  
↓  
Document Retrieval (ChromaDB)  
↓  
Embedding Similarity Search  
↓  
OpenAI Language Model  
↓  
Output Guardrails  
↓  
Response to User

---

## RAG Implementation

The RAG pipeline consists of:

1. Document loading
2. Text processing
3. Creation of text embeddings
4. Storage of embeddings in ChromaDB
5. Similarity-based retrieval of relevant documents
6. Response generation using a language model

The chatbot retrieves information from the knowledge base rather than relying only on the model's pretrained knowledge.

---

## Technologies Used

- Python
- Gradio for the conversational interface
- ChromaDB for vector storage and retrieval
- Sentence Transformers for embeddings
- OpenAI API for response generation
- Git for version control

---

## Memory Implementation

A lightweight conversation memory module was implemented.

The `ConversationMemory` class:

- Stores previous user questions and assistant responses
- Maintains recent conversation history
- Passes previous interactions to the chatbot pipeline

The memory is session-based and resets when the application restarts.

---

## Guardrails Implementation

Input and output validation were implemented to improve reliability.

Input checks include:

- Empty questions
- Missing questions
- Excessively long questions
- Restricted topics

Output checks ensure that empty responses are not returned to users.

---

## Design Decisions

### ChromaDB

ChromaDB was selected as the vector database because it provides a lightweight persistent storage solution suitable for a small RAG application.

### Sentence Transformers

The `all-MiniLM-L6-v2` embedding model was selected because it provides efficient semantic embeddings with low computational requirements.

### OpenAI Model

The language model was used for response generation because it provides strong natural language understanding and generation capabilities.

### Gradio

Gradio was selected because it provides a simple way to create an interactive chatbot interface.

---

## Running the Application

Activate the environment:

```bash
source ~/DSI_projects/deploying-ai/deploying-ai-env/bin/activate

Limitations
The knowledge base is limited to the provided documents.
Conversation memory is session-based and not stored permanently.
Guardrails provide basic validation only.
The chatbot cannot answer questions outside its available knowledge source.


Future Improvements
Possible improvements include:

Persistent user-specific memory
Larger document collections
More advanced safety filtering
Evaluation using automated RAG metrics
