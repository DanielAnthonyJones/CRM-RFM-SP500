# CRM-RFM-SP500
Market Analysis and Stock Segmentation using RFM. Analysis of S&amp;P 500

## Setup

Requires [uv](https://docs.astral.sh/uv/).

    uv sync
    uv run pre-commit install

## Notebook Run order

data_extraction > data_preparation > feature_engineering > clustering

data_extraction will skip download as the compressed CSV file exists in required folder.

## Tests

    uv run pytest
