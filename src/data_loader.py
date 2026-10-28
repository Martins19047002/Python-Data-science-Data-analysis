from pathlib import Path

import pandas as pd


def load_covid_data(path: str | Path) -> pd.DataFrame:
    """Load the Indiana COVID data and normalize it for analysis."""
    data_path = Path(path)
    if not data_path.exists():
        return pd.DataFrame()

    df = pd.read_csv(data_path)

    col_map = {col: col.strip().lower().replace(" ", "_") for col in df.columns}
    df = df.rename(columns=col_map)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    numeric_columns = [
        "new_cases",
        "total_cases",
        "new_deaths",
        "total_deaths",
        "positivity_rate",
        "vaccinated_total",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)
    return df
