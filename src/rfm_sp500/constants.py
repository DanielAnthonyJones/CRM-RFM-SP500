from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TICKER_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"

CONFIG_FILE = BASE_DIR / "config.yaml"
