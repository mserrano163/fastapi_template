# FastAPI Template

This repository contains a template for a basic API built with FastAPI. It provides a starting point for creating robust, high-performance web applications with FastAPI, and is designed to be easily dockerized for consistent deployment across different environments.

## Overview

### FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. FastAPI is easy to use and provides automatic interactive API documentation using Swagger UI and ReDoc.

### Uvicorn

[Uvicorn](https://www.uvicorn.org/) is a lightning-fast ASGI server that serves as the interface between your FastAPI application and the outside world. It is highly performant and designed for modern web frameworks like FastAPI. In this template, Uvicorn is used to run the FastAPI application inside a Docker container.

## Project Structure

- `app.py`: The main FastAPI application file where the FastAPI app is initialized and routes are defined.
- `plugins/`: A directory for reusable components.
  - `__init__.py`: Initializes the `plugins` package and imports utility functions and models.
  - `api_functions.py`: Contains helper functions for API responses.
  - `pydantic_models.py`: Defines Pydantic models used for request validation and serialization.
- `Dockerfile`: Defines the Docker image for the application.
- `Makefile`: Provides convenient commands for building and running the Docker container.
- `requirements.txt`: Lists the dependencies required to run the FastAPI application.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) must be installed on your machine.
- Basic understanding of FastAPI and Docker.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mserrano163/fastapi_template.git
   cd your_repo

2. **Build the Docker Image**
    ```bash
    make build

2. **Run the Docker Container**
    ```bash
    make run


### Accessing the API
Once the container is running, you can access the API at http://localhost:8080. The default route provided in this template is /hello_world, which returns a simple success response.

### Customization
- API Endpoints: Modify app.py to add or change API endpoints.
- Pydantic Models: Update pydantic_models.py to define additional request or response models.
- Docker Configuration: Adjust the Dockerfile and Makefile as needed for your deployment requirements.