"""
Example: Using SysWeld Documentation with LangChain RAG

This script demonstrates how to load and query the SysWeld documentation
using LangChain's RAG capabilities.

Prerequisites:
    pip install langchain langchain-community chromadb openai python-dotenv
    
    Set environment variable: OPENAI_API_KEY
"""

import os
from pathlib import Path
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Configuration
DOCS_PATH = "./docs"
VECTOR_DB_PATH = "./vector_db"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def load_documentation():
    """Load all markdown documentation files."""
    print("Loading documentation...")
    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    return documents


def split_documents(documents):
    """Split documents into chunks for embedding."""
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    splits = text_splitter.split_documents(documents)
    print(f"Created {len(splits)} chunks")
    return splits


def create_vector_store(splits, persist=True):
    """Create vector store from document chunks."""
    print("Creating embeddings and vector store...")
    embeddings = OpenAIEmbeddings()
    
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH if persist else None
    )
    
    if persist:
        print(f"Vector store persisted to {VECTOR_DB_PATH}")
    
    return vectorstore


def load_existing_vector_store():
    """Load a previously created vector store."""
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )
    return vectorstore


def create_qa_chain(vectorstore):
    """Create a question-answering chain."""
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        ),
        return_source_documents=True
    )
    
    return qa_chain


def query_documentation(qa_chain, question):
    """Query the documentation."""
    print(f"\nQuestion: {question}")
    result = qa_chain({"query": question})
    
    print(f"\nAnswer: {result['result']}")
    print("\nSources:")
    for i, doc in enumerate(result['source_documents'], 1):
        source = doc.metadata.get('source', 'Unknown')
        print(f"  {i}. {source}")
    
    return result


def main():
    """Main function to demonstrate RAG with SysWeld documentation."""
    
    # Check if vector store already exists
    vector_store_exists = Path(VECTOR_DB_PATH).exists()
    
    if vector_store_exists:
        print("Loading existing vector store...")
        vectorstore = load_existing_vector_store()
    else:
        # Load and process documentation
        documents = load_documentation()
        splits = split_documents(documents)
        vectorstore = create_vector_store(splits, persist=True)
    
    # Create QA chain
    qa_chain = create_qa_chain(vectorstore)
    
    # Example queries
    example_queries = [
        "How do I install SysWeld on Windows?",
        "What are the system requirements for SysWeld?",
        "How do I set up a welding simulation?",
        "What should I do if I get a mesh generation error?",
        "Explain the thermal analysis workflow in SysWeld"
    ]
    
    print("\n" + "="*60)
    print("SysWeld Documentation RAG System - Example Queries")
    print("="*60)
    
    for query in example_queries:
        result = query_documentation(qa_chain, query)
        print("\n" + "-"*60)
    
    # Interactive mode
    print("\n" + "="*60)
    print("Interactive Mode - Enter 'quit' to exit")
    print("="*60)
    
    while True:
        user_query = input("\nYour question: ").strip()
        if user_query.lower() in ['quit', 'exit', 'q']:
            break
        if user_query:
            query_documentation(qa_chain, user_query)


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set it before running this script:")
        print("  export OPENAI_API_KEY='your-api-key'")
        exit(1)
    
    main()
