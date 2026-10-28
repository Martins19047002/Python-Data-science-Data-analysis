import matplotlib.pyplot as plt

from src.analysis import rolling_average


def plot_trends(df):
    """Generate a trends chart for daily cases and deaths."""
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    if "date" in df.columns and "new_cases" in df.columns:
        axes[0].plot(df["date"], df["new_cases"], label="Daily Cases", color="steelblue", alpha=0.7)
        axes[0].plot(df["date"], rolling_average(df, "new_cases", 7), label="7-day moving average", color="darkorange", linewidth=2)
        axes[0].set_title("Indiana Daily COVID-19 Cases")
        axes[0].set_ylabel("Cases")
        axes[0].legend()

    if "date" in df.columns and "new_deaths" in df.columns:
        axes[1].plot(df["date"], df["new_deaths"], label="Daily Deaths", color="crimson", alpha=0.7)
        axes[1].plot(df["date"], rolling_average(df, "new_deaths", 7), label="7-day moving average", color="darkslategray", linewidth=2)
        axes[1].set_title("Indiana Daily COVID-19 Deaths")
        axes[1].set_ylabel("Deaths")
        axes[1].legend()

    fig.autofmt_xdate()
    fig.tight_layout()
    return fig


def plot_relationships(df):
    """Generate relationship plots for testing and outcomes."""
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    if {"date", "new_cases", "positivity_rate"}.issubset(df.columns):
        axes[0].plot(df["date"], df["new_cases"], color="royalblue")
        axes[0].set_title("Daily Cases Over Time")
        axes[0].set_ylabel("Daily Cases")

        axes[1].plot(df["date"], df["positivity_rate"], color="forestgreen")
        axes[1].set_title("Positivity Rate Over Time")
        axes[1].set_ylabel("Positivity Rate")

    fig.autofmt_xdate()
    fig.tight_layout()
    return fig
