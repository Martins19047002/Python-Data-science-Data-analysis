import pandas as pd


def compute_summary(df: pd.DataFrame) -> dict:
    """Compute summary metrics for the Indiana COVID-19 dataset."""
    summary = {
        "total_cases": int(df["total_cases"].fillna(0).iloc[-1]) if "total_cases" in df.columns else 0,
        "total_deaths": int(df["total_deaths"].fillna(0).iloc[-1]) if "total_deaths" in df.columns else 0,
        "peak_cases_per_day": int(df["new_cases"].max()) if "new_cases" in df.columns else 0,
        "peak_deaths_per_day": int(df["new_deaths"].max()) if "new_deaths" in df.columns else 0,
    }
    return summary


def rolling_average(df: pd.DataFrame, column: str, window: int = 7) -> pd.Series:
    """Create a rolling average series for a column."""
    if column not in df.columns:
        return pd.Series(index=df.index, dtype=float)
    return df[column].rolling(window=window, min_periods=1).mean()


def hypothesis_summary(df: pd.DataFrame) -> list[str]:
    """Return text-based hypothesis statements for reporting."""
    hypotheses = [
        "H1: Indiana experienced distinct COVID-19 wave periods with elevated daily case spikes.",
        "H2: Vaccination rollout was associated with lower severe disease outcomes after early rollout phases.",
        "H3: Higher testing volume and positivity rate were associated with greater case detection, though the relationship is complex.",
        "H4: Case and mortality trends did not always move in synchrony because of reporting lag and changing public health conditions."
    ]
    return hypotheses
