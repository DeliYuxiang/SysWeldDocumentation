# RAG Integration Examples

This directory contains example scripts demonstrating how to use the SysWeld documentation as a RAG (Retrieval-Augmented Generation) source.

## Available Examples

### 1. LangChain RAG (`langchain_rag.py`)

Demonstrates integration with LangChain using Chroma vector store.

**Installation:**
```bash
pip install langchain langchain-community chromadb openai python-dotenv
```

**Usage:**
```bash
export OPENAI_API_KEY='your-api-key-here'
python langchain_rag.py
```

**Features:**
- Loads all markdown documentation
- Creates embeddings using OpenAI
- Stores vectors in Chroma DB
- Provides Q&A interface
- Shows source documents for answers

### 2. LlamaIndex RAG (`llamaindex_rag.py`)

Demonstrates integration with LlamaIndex.

**Installation:**
```bash
pip install llama-index openai python-dotenv
```

**Usage:**
```bash
export OPENAI_API_KEY='your-api-key-here'
python llamaindex_rag.py
```

**Features:**
- Simple document loading
- Efficient indexing
- Query engine with source attribution
- Persistent storage

## Requirements

All examples require:
- Python 3.8+
- OpenAI API key (or alternative LLM provider)
- The SysWeld documentation in `../docs/` directory

## Configuration

### Using Different Embedding Models

**LangChain with HuggingFace:**
```python
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

**LlamaIndex with local models:**
```python
from llama_index.embeddings import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-large-en-v1.5"
)
```

### Using Different Vector Stores

**Pinecone:**
```python
import pinecone
from langchain.vectorstores import Pinecone

pinecone.init(api_key="your-key", environment="your-env")
vectorstore = Pinecone.from_documents(splits, embeddings, index_name="sysweld-docs")
```

**Weaviate:**
```python
import weaviate
from langchain.vectorstores import Weaviate

client = weaviate.Client("http://localhost:8080")
vectorstore = Weaviate.from_documents(splits, embeddings, client=client)
```

## Customization

### Adjusting Chunk Size

Modify these parameters based on your needs:

```python
CHUNK_SIZE = 1000      # Size of each text chunk
CHUNK_OVERLAP = 200    # Overlap between chunks
```

Larger chunks provide more context but reduce granularity. Smaller chunks improve precision but may lose context.

### Changing Retrieval Parameters

```python
# Number of documents to retrieve
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# Use MMR (Maximum Marginal Relevance) for diversity
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4, "fetch_k": 10}
)
```

## Example Queries

Try these questions with the examples:

**Getting Started:**
- "How do I install SysWeld?"
- "What are the system requirements?"
- "How do I activate my license?"

**Technical Questions:**
- "How do I set up a butt weld simulation?"
- "What mesh size should I use?"
- "How do I define welding parameters?"

**Troubleshooting:**
- "My simulation won't converge, what should I do?"
- "I'm getting mesh generation errors, how do I fix them?"
- "What does error code E001 mean?"

## Performance Tips

1. **First run**: Building the index takes time. Subsequent runs load from cache.
2. **Incremental updates**: Rebuild index when documentation changes.
3. **Batch queries**: Process multiple queries in one session to reuse loaded index.
4. **Hardware**: Use GPU-accelerated embeddings for faster processing.

## Advanced Usage

### Creating a Web API

Use FastAPI to create a REST API:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load index once at startup
@app.on_event("startup")
async def startup_event():
    global query_engine
    index = load_index()
    query_engine = index.as_query_engine()

class Query(BaseModel):
    question: str

@app.post("/query")
async def query(query: Query):
    response = query_engine.query(query.question)
    return {"answer": str(response)}
```

### Adding Conversation Memory

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)
```

## Troubleshooting

**Issue**: "Rate limit exceeded"
- Solution: Add retry logic or use a different LLM provider

**Issue**: "Out of memory"
- Solution: Process documents in batches, reduce chunk size, or use a smaller embedding model

**Issue**: "Poor answer quality"
- Solution: Adjust chunk size/overlap, increase k (number of retrieved documents), or improve documentation quality

## Contributing

To add more examples:
1. Create a new Python file
2. Follow the existing structure
3. Document prerequisites and usage
4. Add to this README

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Chroma Documentation](https://docs.trychroma.com/)
