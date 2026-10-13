from datetime import datetime

import pytest
import yaml


@pytest.fixture(scope="module")
def config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)


# Tests


def test_valid_date(config):
    """
    Test that the start and end dates in the config file are valid dates in YYYY-MM-DD format.
    """
    for key in ["start_date", "end_date_exclusive"]:
        # raises ValueError if the date is not valid
        datetime.strptime(config[key], "%Y-%m-%d")


def test_random_seed_is_an_integer(config):
    """
    Test that the random seed is integer.
    """
    seed = config["random_seed"]
    assert isinstance(seed, int)


def test_benchmark(config):
    """
    Test that the benchmark is set to "^GSPC".
    """
    assert config["benchmark"] == "^GSPC"
