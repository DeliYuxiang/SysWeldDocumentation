"""
Example: Using SysWeld Documentation with LlamaIndex

This script demonstrates how to load and query the SysWeld documentation
using LlamaIndex's RAG capabilities.

Prerequisites:
    pip install llama-index openai python-dotenv
    
    Set environment variable: OPENAI_API_KEY
"""

import os
from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage
)
from llama_index.llms import OpenAI

# Configuration
DOCS_PATH = "./docs"
STORAGE_PATH = "./storage"


def build_index():
    """Build index from documentation."""
    print("Loading documents from:", DOCS_PATH)
    
    # Load all markdown files
    documents = SimpleDirectoryReader(
        DOCS_PATH,
        recursive=True,
        required_exts=[".md"]
    ).load_data()
    
    print(f"Loaded {len(documents)} documents")
    
    # Create index
    print("Building index...")
    index = VectorStoreIndex.from_documents(documents)
    
    # Persist index
    print(f"Persisting index to {STORAGE_PATH}...")
    index.storage_context.persist(persist_dir=STORAGE_PATH)
    
    return index


def load_index():
    """Load existing index."""
    print("Loading existing index from:", STORAGE_PATH)
    storage_context = StorageContext.from_defaults(persist_dir=STORAGE_PATH)
    index = load_index_from_storage(storage_context)
    return index


def query_documentation(query_engine, question):
    """Query the documentation."""
    print(f"\nQuestion: {question}")
    response = query_engine.query(question)
    
    print(f"\nAnswer: {response}")
    
    # Show source nodes if available
    if hasattr(response, 'source_nodes') and response.source_nodes:
        print("\nSources:")
        for i, node in enumerate(response.source_nodes, 1):
            metadata = node.node.metadata
            source = metadata.get('file_path', 'Unknown')
            print(f"  {i}. {source}")
    
    return response


def main():
    """Main function to demonstrate RAG with SysWeld documentation."""
    
    # Check if index exists
    if os.path.exists(STORAGE_PATH):
        index = load_index()
    else:
        index = build_index()
    
    # Configure LLM
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create query engine
    query_engine = index.as_query_engine(
        llm=llm,
        similarity_top_k=4
    )
    
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
        response = query_documentation(query_engine, query)
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
            query_documentation(query_engine, user_query)


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set it before running this script:")
        print("  export OPENAI_API_KEY='your-api-key'")
        exit(1)
    
    main()
