# Indiana COVID-19 Data Analysis Project

This repository is a data science portfolio project focused on COVID-19 trends in Indiana. It combines a literature review, four hypothesis-driven research questions, trend analysis, and a simple dashboard for communicating the findings.

## Project overview

The main goal of this project is to examine how COVID-19 changed over time in Indiana and to highlight patterns in cases, deaths, testing positivity, and vaccination trends. The project is designed to show a realistic end-to-end workflow used in applied data analysis and public health research.

## Research questions

1. How did COVID-19 cases and deaths change over time in Indiana?
2. Were there distinct outbreak waves across the study period?
3. Did vaccination growth align with changes in severe outcomes?
4. How did testing intensity and positivity rate relate to observed case patterns?

## Hypotheses

1. Indiana experienced multiple COVID-19 waves with clear periods of elevated cases.
2. Vaccination rollout was associated with lower severe disease outcomes during later phases of the pandemic.
3. Higher testing volume was associated with more case detection, but should be interpreted alongside positivity rate and deaths.
4. Case counts and mortality did not always move in lockstep because of reporting lag, healthcare effects, and public health response patterns.

## Tools used

- Python
- Jupyter Notebook
- pandas
- NumPy
- matplotlib
- seaborn
- Plotly
- Streamlit
- SciPy
- GitHub

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
│   ├── hypotheses.md
│   └── literature_review.md
├── notebooks/
│   └── covid_indiana_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analysis.py
│   └── visualization.py
├── reports/
│   └── summary.md
└── LICENSE
```

## Dataset source

This project uses a sample Indiana COVID-19 dataset for demonstration and portfolio use. For a final analysis, you can replace it with official public health data from:

- Indiana State Department of Health: https://www.in.gov/isdh/
- CDC COVID Data Tracker: https://covid.cdc.gov/covid-data-tracker/
- Our World in Data: https://ourworldindata.org/covid-deaths

## Literature review

The project includes a concise literature review in `docs/literature_review.md` covering:

- epidemic waves and transmission dynamics
- testing and surveillance systems
- vaccination and severe outcomes
- public health dashboards and communication

## Notebook workflow

The Jupyter Notebook in `notebooks/covid_indiana_analysis.ipynb` contains:

- data loading
- trend analysis
- visual exploration
- moving averages
- hypothesis summary
- final interpretation

## Dashboard app

The Streamlit dashboard in `app.py` allows you to:

- inspect daily case and death trends
- review moving-average patterns
- compare positivity and vaccination trends
- summarize key hypotheses visually

## Running the project locally

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open the notebook

```bash
jupyter notebook notebooks/covid_indiana_analysis.ipynb
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

## Files included

- `README.md`: project overview and setup instructions
- `requirements.txt`: required Python packages
- `app.py`: interactive dashboard
- `data/indiana_covid19_sample.csv`: local sample dataset
- `docs/literature_review.md`: literature review
- `docs/hypotheses.md`: hypothesis summary
- `reports/summary.md`: final report summary
- `src/analysis.py`: calculations and hypothesis outputs
- `src/data_loader.py`: data loading and cleaning
- `src/visualization.py`: charts and dashboard visuals

## Portfolio use

This project is suitable for a data science portfolio because it demonstrates:

- data cleaning and preparation
- time-series analysis
- public health interpretation
- notebook-based analysis workflow
- dashboard storytelling
- hypothesis-driven research

## License

This project is intended for educational and portfolio use.

---

If you want to take this project further, the next improvement would be to add county-level maps, time-series forecasting, or a more advanced public health dashboard.
