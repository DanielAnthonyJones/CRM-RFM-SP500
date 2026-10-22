import numpy as np
import pandas as pd

from rfm_sp500.validation import get_nan_summary

nan = np.nan


def create_df(**columns):
    """Create small df with given columns for testing.
    Requires date column as its dropped in function
    """
    return pd.DataFrame({"Date": nan, **columns})


def test_no_missing_values():
    df = create_df(Close=[1, 2, 3], Volume=[1, 2, 3])
    summary, middle = get_nan_summary(df)

    assert summary == {"Leading": 0, "Trailing": 0}
    assert middle == {"Close": 0, "Volume": 0}


def test_leading_nans_same_every_column():

    df = create_df(Close=[nan, nan, 1, 2], Volume=[nan, nan, 1, 2])

    summary, middle = get_nan_summary(df)

    assert summary["Leading"] == 2
    assert summary["Trailing"] == 0
    assert middle == {"Close": 0, "Volume": 0}


def test_trailing_nans_same_every_column():

    df = create_df(Close=[1, 2, nan], Volume=[1, 2, nan])

    summary, _ = get_nan_summary(df)

    assert summary["Leading"] == 0
    assert summary["Trailing"] == 1


def test_gap_in_middle():

    df = create_df(Close=[1, nan, nan, 2], Volume=[1, 2, 3, 4])

    summary, middle = get_nan_summary(df)

    assert middle == {"Close": 2, "Volume": 0}
    assert summary == {"Leading": 0, "Trailing": 0}


def test_different_per_column():

    df = create_df(Close=[nan, 2.0, nan, nan, nan], Volume=[10.0, nan, nan, nan, nan])

    summary, _ = get_nan_summary(df)

    assert summary["Leading"] == "different counts per column"
    assert summary["Trailing"] == "different counts per column"


def test_empty_ticker():

    df = create_df(Close=[nan, nan, nan], Volume=[nan, nan, nan])

    summary, middle = get_nan_summary(df)

    assert summary == {"Leading": None, "Trailing": None}
    assert middle == {"Close": 0, "Volume": 0}


def test_counts_are_int():
    """Reason is because yaml has issues saving non python int, and id probably
    not notice the issue in my code"""

    df = create_df(Close=[nan, 1.0, nan, 2.0])

    summary, middle = get_nan_summary(df)

    assert type(summary["Leading"]) is int
    assert type(middle["Close"]) is int
