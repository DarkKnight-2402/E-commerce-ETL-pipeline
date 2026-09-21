# E-Commerce ETL Pipeline

## Overview

A Python-based ETL pipeline that extracts e-commerce product data
from a REST API, transforms and validates the data using Pandas,
and loads the processed dataset into SQLite for SQL-based analysis.

## Architecture

REST API
    ↓
Python Requests
    ↓
Raw JSON
    ↓
Pandas
    ↓
Data Cleaning & Validation
    ↓
Processed CSV
    ↓
SQLite
    ↓
SQL Analytics

## Technologies

- Python
- Requests
- Pandas
- SQL
- SQLite
- Git

## Project Structure

```text
ecommerce-etl/
├── data/
│   ├── raw/
│   ├── processed/
│   └── ecommerce.db
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── analytics.sql
└── README.md