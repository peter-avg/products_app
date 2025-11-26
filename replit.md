# Products App

## Overview
This is a FastAPI-based product management application that uses OpenAI to automatically generate product tags. The application provides a RESTful API for creating, reading, and managing products with AI-powered tagging capabilities.

## Project Structure
- `app/` - Main application directory
  - `api.py` - FastAPI routes and endpoints
  - `schemas.py` - Pydantic schemas for data validation
  - `db/` - Database configuration and utilities
    - `config.py` - Database connection setup (SQLite)
    - `schemas.py` - SQLAlchemy database models
    - `utils.py` - Database utility functions
  - `llm/` - OpenAI integration
    - `config.py` - OpenAI client configuration
    - `prompts.py` - AI prompt templates
    - `utils.py` - LLM utility functions
- `main.py` - Application entry point

## Technology Stack
- **Framework**: FastAPI
- **Database**: SQLite (SQLAlchemy ORM)
- **AI Integration**: OpenAI GPT-4o-mini
- **Package Manager**: uv
- **Python Version**: 3.12

## Configuration
- The application runs on port 5000 (configured for Replit's web preview)
- OpenAI API key is stored in Replit Secrets as `OPENAI_API_KEY`
- Database file: `notes.db` (SQLite)

## API Endpoints
- `GET /` - Root endpoint (health check)
- `POST /products` - Create a product with JSON body
- `POST /products/{name}/{description}` - Create a product with URL parameters
- `GET /products` - Get all products
- `GET /products/{product_id}` - Get a specific product
- `GET /tags/{product_id}` - Get AI-generated tags for a product
- `POST /products/{product_id}/regenerate_tags` - Regenerate tags for a product
- `DELETE /products/{product_id}` - Delete a specific product
- `DELETE /delete_all` - Delete all products

## Recent Changes (November 26, 2025)
- Configured project for Replit environment
- Updated Python version requirement from 3.13 to 3.12
- Configured uvicorn to run on 0.0.0.0:5000 for web preview
- Set up OpenAI API key integration via Replit Secrets
- Updated .gitignore for uv and Python artifacts
- Configured deployment settings for autoscale

## Development
- Dependencies are managed with `uv` and defined in `pyproject.toml`
- Run `uv sync` to install dependencies
- The workflow automatically runs the FastAPI server with hot reload enabled

## Deployment
- Deployment target: Autoscale (stateless API)
- Production server: uvicorn on port 5000
- Secrets required: OPENAI_API_KEY
