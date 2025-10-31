# SysWeld Documentation

This repository contains comprehensive documentation for SysWeld Software, structured and optimized for use as a **RAG (Retrieval-Augmented Generation) source**.

## Overview

SysWeld is a welding simulation software, and this documentation repository serves as a knowledge base that can be integrated with AI systems, chatbots, and other applications that utilize RAG techniques.

## Repository Structure

```
SysWeldDocumentation/
├── docs/                    # Main documentation directory
│   ├── getting-started/    # Beginner guides and tutorials
│   ├── user-guide/         # Detailed user documentation
│   ├── api-reference/      # API documentation
│   ├── tutorials/          # Step-by-step tutorials
│   └── troubleshooting/    # Common issues and solutions
├── metadata.json           # Repository metadata for RAG systems
└── README.md              # This file
```

## Using as a RAG Source

### Quick Start

This repository is designed to be easily integrated into RAG pipelines:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DeliYuxiang/SysWeldDocumentation.git
   cd SysWeldDocumentation
   ```

2. **Point your RAG system to the `docs/` directory**:
   - All documentation files are in Markdown format
   - Each file includes metadata headers for better context
   - Files are organized hierarchically by topic

### Integration Examples

#### With LangChain

```python
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Load documents
loader = DirectoryLoader(
    './docs',
    glob="**/*.md",
    loader_cls=TextLoader
)
documents = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings
)
```

#### With LlamaIndex

```python
from llama_index import SimpleDirectoryReader, VectorStoreIndex

# Load documents
documents = SimpleDirectoryReader('./docs').load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("How do I start a welding simulation?")
```

### Document Format

All documentation follows these conventions:

- **Format**: Markdown (.md)
- **Encoding**: UTF-8
- **Structure**: Clear hierarchical headings (H1-H6)
- **Metadata**: YAML frontmatter where applicable
- **Links**: Relative links within the repository

### Metadata

The `metadata.json` file contains:
- Repository information
- Document categorization
- Version information
- Topic tags for better retrieval

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new documentation
- Updating existing content
- Formatting standards
- Review process

## Documentation Guidelines

### File Naming
- Use lowercase with hyphens: `welding-parameters.md`
- Be descriptive: `thermal-analysis-setup.md` not `setup.md`
- Group related files in directories

### Content Structure
1. Start with a clear title (H1)
2. Include a brief overview
3. Use consistent heading hierarchy
4. Add code examples where relevant
5. Include troubleshooting tips
6. End with related links

### Markdown Features
- Use code blocks with language tags
- Include tables for structured data
- Add lists for step-by-step instructions
- Use bold for emphasis, italics for terms
- Include images in an `images/` subdirectory

## RAG Optimization Tips

1. **Chunk-friendly structure**: Keep sections focused and self-contained
2. **Clear headings**: Use descriptive headings for better semantic search
3. **Context inclusion**: Each section should be understandable independently
4. **Keywords**: Include relevant technical terms naturally
5. **Cross-references**: Link related topics for better context

## Version

Current version: 1.0.0

## License

This documentation is provided for educational and reference purposes. See [LICENSE](LICENSE) for details.

## Support

For questions or issues:
- Open an issue in this repository
- Contact the SysWeld documentation team
- Check the troubleshooting section in docs/

## Acknowledgments

This repository structure is optimized for RAG systems including:
- LangChain
- LlamaIndex
- Haystack
- Custom embedding pipelines
- Vector databases (Chroma, Pinecone, Weaviate, etc.)