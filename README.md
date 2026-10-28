# COVID-19 in Indiana: Trend Analysis and Hypothesis-Driven Research

This repository contains a data science project focused on understanding COVID-19 trends in Indiana. The project combines exploratory data analysis, literature review, hypothesis testing, and a simple interactive dashboard to communicate findings clearly.

## Project goals

- Analyze Indiana COVID-19 trends over time
- Identify patterns in cases, deaths, testing, and vaccination indicators
- Explore how public health events and policy changes may relate to observed trends
- Develop and test four research hypotheses
- Present findings in a simple dashboard and notebook workflow

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── app.py
├── .gitignore
├── data/
│   ├── README.md
│   └── indiana_covid19_sample.csv
├── docs/
│   ├── literature_review.md
│   └── hypotheses.md
├── notebooks/
│   └── covid_indiana_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analysis.py
│   └── visualization.py
└── reports/
    └── summary.md
```

## Suggested tools

To make the project clear and presentation-ready, the following tools are recommended:

- Python for analysis and scripting
- Jupyter Notebook for exploratory analysis
- pandas for data cleaning and transformation
- NumPy for numerical analysis
- matplotlib and seaborn for static charts
- Plotly for interactive visuals
- Streamlit for a lightweight dashboard
- GitHub for version control and portfolio presentation
- Optional: GeoPandas for county-level maps if you later expand the analysis

## Dataset source

This project uses a sample Indiana COVID-19 time series dataset suitable for a portfolio and demonstration.

Recommended public data sources for real-world expansion:

- Indiana State Department of Health COVID-19 dashboard: https://www.in.gov/isdh/ 
- CDC COVID Data Tracker: https://covid.cdc.gov/covid-data-tracker/
- Our World in Data COVID-19 dataset: https://ourworldindata.org/covid-deaths

Important note:
This repository includes a sample CSV for local use. For a full research project, replace it with official Indiana surveillance data or a county-level dataset from Indiana public health sources.

## Research questions and hypotheses

The project explores the following questions:

1. How did infection counts and deaths change across different time periods in Indiana?
2. Did vaccination rollout align with reduced severe outcomes over time?
3. Were there notable surges during specific seasonal or epidemiological periods?
4. Did testing volume and positivity trends help explain the dynamics of the epidemic?

### Hypotheses

1. There were distinct pandemic waves in Indiana, with the highest case counts during major surge periods.
2. Vaccination coverage was associated with a reduction in severe outcomes after early rollout periods.
3. Higher testing volume was associated with increased daily case detection, but not necessarily with sustained growth in mortality.
4. Counties with greater testing intensity showed more consistent early detection and faster public health response patterns.

See `docs/hypotheses.md` for a more detailed version.

## Literature review

This project includes a concise literature review in `docs/literature_review.md` covering themes such as:

- COVID-19 epidemiological trends
- public health surveillance systems
- vaccination and outcome changes
- temporal dynamics of epidemic waves
- the value of dashboards in public health communication

## Analysis workflow

1. Load and inspect the dataset
2. Clean missing or inconsistent values
3. Convert date columns to datetime format
4. Compute rolling averages for trend analysis
5. Visualize cases, deaths, positivity, and vaccination indicators
6. Evaluate the four hypotheses
7. Summarize findings in a dashboard and narrative report

## Jupyter notebook

The notebook for exploratory analysis is located here:

- `notebooks/covid_indiana_analysis.ipynb`

It includes:

- setup and package import section
- dataset loading
- exploratory data analysis
- trend analysis
- plotting
- hypothesis summary

## Dashboard app

The Streamlit dashboard is located here:

- `app.py`

It allows you to:

- view daily and moving-average trends
- compare cases and deaths
- inspect positivity and vaccination patterns
- summarize the research findings in a reusable format

## Run locally

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

Open the notebook in Jupyter:

```bash
jupyter notebook notebooks/covid_indiana_analysis.ipynb
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

## Expected outputs

- Cleaned dataset ready for analysis
- Trend charts showing COVID surges and declines
- Jupyter analysis workflow for reproducibility
- Dashboard for interactive exploration
- Research summary and literature review
- Hypothesis-driven analysis for portfolio use

## Notes for improvement

For a stronger final portfolio version, consider adding:

- county-level maps using GeoPandas
- seasonal decomposition
- ARIMA time series modeling
- machine learning forecasting
- comparative analysis with another state or national data

## License

This project is for educational and portfolio use.

---

If you want a more advanced portfolio version, consider expanding this into a full public health data analysis project with county-level maps, dashboards, and a polished narrative report.
