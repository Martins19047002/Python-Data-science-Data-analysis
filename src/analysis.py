import pandas as pd


def compute_summary(df: pd.DataFrame) -> dict:
    """Return summary statistics for the Indiana COVID dataset."""
    summary = {
        "total_cases": int(df["total_cases"].fillna(0).iloc[-1]) if "total_cases" in df.columns else 0,
        "total_deaths": int(df["total_deaths"].fillna(0).iloc[-1]) if "total_deaths" in df.columns else 0,
        "peak_cases_per_day": int(df["new_cases"].max()) if "new_cases" in df.columns else 0,
        "peak_deaths_per_day": int(df["new_deaths"].max()) if "new_deaths" in df.columns else 0,
    }
    return summary


def rolling_average(df: pd.DataFrame, column: str, window: int = 7) -> pd.Series:
    """Return a rolling average for a time series column."""
    if column not in df.columns:
        return pd.Series(index=df.index, dtype=float)
    return df[column].rolling(window=window, min_periods=1).mean()


def hypothesis_summary(df: pd.DataFrame) -> list[str]:
    """Create text summaries for the four project hypotheses."""
    hypotheses = [
        "H1: Indiana experienced distinct COVID-19 waves, with significant daily case spikes during outbreak periods.",
        "H2: Vaccination rollout trends were associated with lower severe outcomes after initial rollout phases.",
        "H3: Testing intensity explains part of the observed case pattern, because higher testing volume often leads to more case detection.",
        "H4: Case trends and mortality trends changed at different rates over time, suggesting dynamic public health responses and immunity effects."
    ]
    return hypotheses
