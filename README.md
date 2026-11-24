# CRM-RFM-SP500
Market Analysis and Stock Segmentation using RFM. Analysis of S&amp;P 500

## Setup

Requires [uv](https://docs.astral.sh/uv/).

    uv sync
    uv run pre-commit install

## Notebook Run order

data_extraction > data_preparation > feature_engineering > clustering

data_extraction will skip download as the compressed CSV file exists in `data/raw`.

## Study settings

- Study period: 2021-01-01 to 2025-01-01 (end date exclusive), benchmark ^GSPC
- Observation date: 2024-12-31
- Data downloaded 20 October 2026 with yfinance 1.7.0 (see `data/raw/metadata.yaml`)
- Random seed: 123 (`config.yaml`)


## Where to find things

- Raw data snapshots and ticker list: `data/raw/`
- Exclusions with reasons: `data/processed/exclusion_dict_2021-01-01_2025-01-01.yaml`
- Feature table (494 shares) with cluster assignments for all four solutions:
  `data/processed/features_with_clusters.csv.gz`
- Figures used in the report: `outputs/figures/`
- Package versions: `uv.lock` and `requirements.txt`

## Tests

    uv run pytest
