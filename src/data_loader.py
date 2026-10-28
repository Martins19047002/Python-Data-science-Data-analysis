from pathlib import Path
import pandas as pd


def load_covid_data(path: str | Path) -> pd.DataFrame:
    """Load the Indiana COVID dataset and standardize column names."""
    data_path = Path(path)
    if not data_path.exists():
        return pd.DataFrame()

    df = pd.read_csv(data_path)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    for col in ["new_cases", "total_cases", "new_deaths", "total_deaths", "positivity_rate", "vaccinated_total"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)
    return df
