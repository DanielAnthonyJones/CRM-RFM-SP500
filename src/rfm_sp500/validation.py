import pandas as pd


def get_nan_summary(df: pd.DataFrame) -> tuple[dict, dict]:
    """
    Reports missing values (NaNs) for a ticker's history

    df : Dataframe
        Rows for a single ticker ordered by date

    Returns:
        summary: dict

            "Leading" - number of NaNs before first valid value if every column has the same value
            "Trailing" - same as above but for after last valid value
            Value will be None if every column is empty or string if different counts per column

        missing_in_middle : dict
            NaN count between first and last valid value per column

    """
    df = df.drop(columns=["Date"])
    df = df.reset_index(drop=True)

    summary = {"Leading": None, "Trailing": None}

    missing_in_middle = {col: 0 for col in df.columns}
    leading_counts = {}
    trailing_counts = {}

    for col in df.columns:
        first = df[col].first_valid_index()

        if first is None:
            continue

        last = df[col].last_valid_index()

        middle = df[col].loc[first:last].isna()
        missing_in_middle[col] = int(middle.sum())

        leading_counts[col] = int(first)
        trailing_counts[col] = int(len(df) - 1 - last)

    if leading_counts:
        unique_leading = set(leading_counts.values())

        if len(unique_leading) == 1:
            summary["Leading"] = next(iter(unique_leading))
        else:
            summary["Leading"] = "different counts per column"

    if trailing_counts:
        unique_trailing = set(trailing_counts.values())

        if len(unique_trailing) == 1:
            summary["Trailing"] = next(iter(unique_trailing))
        else:
            summary["Trailing"] = "different counts per column"

    return (summary, missing_in_middle)
