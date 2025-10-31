---
title: API Reference Overview
category: api-reference
topics: [api, scripting, automation, programming]
difficulty: advanced
last_updated: 2025-10-31
---

# API Reference

Technical documentation for SysWeld automation and scripting.

## Overview

The SysWeld API enables:
- Automation of repetitive tasks
- Batch processing of simulations
- Custom workflow development
- Integration with other tools

## Available APIs

- **Python API**: Full-featured scripting interface
- **Command Line Interface**: Batch mode execution
- **REST API**: Web service integration (advanced versions)

## Getting Started with API

Basic example:
```python
import sysweld

# Create a new project
project = sysweld.Project("MyProject")

# Load geometry
project.load_geometry("model.step")

# Setup and run
project.setup_welding(parameters)
project.run_analysis()
```

More detailed API documentation coming soon.
