# Contributing to SysWeld Documentation

Thank you for your interest in contributing to the SysWeld Documentation repository! This document provides guidelines for adding and updating documentation.

## Table of Contents

- [Getting Started](#getting-started)
- [Documentation Standards](#documentation-standards)
- [File Organization](#file-organization)
- [Writing Guidelines](#writing-guidelines)
- [Submission Process](#submission-process)
- [RAG Optimization](#rag-optimization)

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your changes
4. Make your changes following these guidelines
5. Submit a pull request

## Documentation Standards

### File Format

All documentation must be in **Markdown (.md)** format with:
- UTF-8 encoding
- Unix-style line endings (LF)
- No trailing whitespace
- Blank line at end of file

### Frontmatter

Include YAML frontmatter at the beginning of each document:

```yaml
---
title: Document Title Here
category: getting-started
topics: [installation, setup, configuration]
difficulty: beginner
last_updated: 2025-10-31
related:
  - ../user-guide/basic-concepts.md
  - ../tutorials/first-simulation.md
---
```

**Fields:**
- `title`: Clear, descriptive title (required)
- `category`: One of: getting-started, user-guide, api-reference, tutorials, troubleshooting (required)
- `topics`: Array of relevant keywords (required)
- `difficulty`: beginner, intermediate, or advanced (required)
- `last_updated`: Date in YYYY-MM-DD format (required)
- `related`: Array of related document paths (optional)

## File Organization

### Directory Structure

```
docs/
├── getting-started/
│   ├── installation.md
│   ├── quickstart.md
│   └── basic-concepts.md
├── user-guide/
│   ├── interface/
│   ├── workflows/
│   └── advanced-features/
├── api-reference/
│   ├── scripting/
│   └── automation/
├── tutorials/
│   ├── welding-simulation/
│   └── thermal-analysis/
└── troubleshooting/
    ├── common-errors.md
    └── faq.md
```

### File Naming

- Use lowercase letters
- Use hyphens for spaces: `welding-parameters.md`
- Be descriptive: `thermal-analysis-setup.md` not `setup.md`
- Keep names concise but clear

### Images and Assets

- Store images in an `images/` subdirectory within each category
- Use descriptive filenames: `welding-interface-overview.png`
- Optimize image sizes (prefer PNG for screenshots, JPG for photos)
- Use relative paths: `![Interface](./images/welding-interface.png)`

## Writing Guidelines

### Content Structure

1. **Title (H1)**: One per document, clear and descriptive
2. **Introduction**: Brief overview (2-3 sentences)
3. **Main Content**: Organized with clear headings
4. **Examples**: Include practical examples
5. **Related Topics**: Links to related documentation
6. **Troubleshooting**: Common issues if applicable

### Heading Hierarchy

```markdown
# Main Title (H1) - One per document

## Major Section (H2)

### Subsection (H3)

#### Minor Section (H4)

##### Detail Section (H5)

###### Fine Detail (H6)
```

### Code Blocks

Always specify the language for syntax highlighting:

````markdown
```python
import sysweld

# Example code
simulation = sysweld.Simulation()
```
````

### Lists

**Unordered lists:**
```markdown
- First item
- Second item
  - Sub-item
  - Another sub-item
```

**Ordered lists:**
```markdown
1. First step
2. Second step
3. Third step
```

### Tables

Use tables for structured data:

```markdown
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| temperature | float | 20.0 | Initial temperature in °C |
| material | string | "Steel" | Material type |
```

### Emphasis

- **Bold** for important terms: `**important**`
- *Italic* for technical terms: `*parameter*`
- `Code` for inline code: `` `variable_name` ``

### Links

- Use relative links within the repository: `[Basic Concepts](../getting-started/basic-concepts.md)`
- Use descriptive link text: `[installation guide](./installation.md)` not `[click here](./installation.md)`
- External links should open in new window when converted to HTML

## Submission Process

### Before Submitting

1. **Review your changes**: Read through your documentation
2. **Check formatting**: Ensure proper Markdown syntax
3. **Verify links**: All internal links work correctly
4. **Test code examples**: If included, verify they work
5. **Update metadata**: Ensure frontmatter is complete and accurate
6. **Check spelling**: Use a spell checker

### Pull Request Guidelines

**PR Title Format:**
```
[Category] Brief description of changes

Examples:
[Getting Started] Add installation guide for Windows
[Tutorials] Update thermal analysis tutorial
[Troubleshooting] Add common error solutions
```

**PR Description:**
- Summarize what was added/changed
- Explain why the change was needed
- List any related issues
- Note any breaking changes

### Review Process

- PRs require review before merging
- Address reviewer feedback promptly
- Keep discussions constructive and professional
- Update documentation based on feedback

## RAG Optimization

### Writing for RAG Systems

To optimize documentation for RAG (Retrieval-Augmented Generation):

1. **Self-contained sections**: Each section should make sense independently
2. **Clear context**: Include necessary context in each section
3. **Descriptive headings**: Use headings that clearly describe content
4. **Keywords**: Include relevant technical terms naturally
5. **Consistent terminology**: Use the same terms throughout
6. **Avoid ambiguous references**: Don't rely heavily on "this", "that", "above", "below"

### Chunk-Friendly Writing

- Keep paragraphs focused (3-5 sentences)
- Use clear topic sentences
- Break long sections into subsections
- Include transitions between topics

### Example: Good vs. Bad

**Bad (for RAG):**
```markdown
## Setup

First, do this. Then do that. See above for details.
```

**Good (for RAG):**
```markdown
## SysWeld Installation Setup

To install SysWeld on Windows, follow these steps:

1. Download the installer from the official website
2. Run the installer with administrator privileges
3. Select your installation directory (default: C:\Program Files\SysWeld)
4. Choose the components to install (Full installation recommended)
```

### Metadata Best Practices

- Use specific, relevant topics
- Include synonyms in content
- Cross-reference related documents
- Update last_updated date when editing
- Choose appropriate difficulty level

## Questions?

If you have questions about contributing:
- Open an issue with the `question` label
- Check existing issues for similar questions
- Review existing documentation as examples

## Code of Conduct

- Be respectful and professional
- Provide constructive feedback
- Help create a welcoming environment
- Focus on the documentation, not the person

Thank you for helping improve SysWeld documentation!
