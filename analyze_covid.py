#!/usr/bin/env python3
"""Clean and summarize the included Our World in Data COVID-19 extract.
Run: python python/analyze_covid.py data/covid_dashboard_data.csv
"""
from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt

INPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/covid_dashboard_data.csv")
OUT = Path("output")
OUT.mkdir(exist_ok=True)
df = pd.read_csv(INPUT, parse_dates=["date"])
required = {"location", "date", "total_cases", "total_deaths", "new_cases_smoothed", "total_cases_per_million"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")
for col in ["total_cases", "total_deaths", "new_cases_smoothed", "total_cases_per_million", "total_deaths_per_million", "people_fully_vaccinated_per_hundred"]:
    if col in df:
        df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["location", "date"]).sort_values(["location", "date"])
df.to_csv(OUT / "covid_cleaned.csv", index=False, date_format="%Y-%m-%d")
world = df[(df.location == "World") & df.new_cases_smoothed.notna()]
if not world.empty:
    plt.figure(figsize=(10, 5))
    plt.plot(world.date, world.new_cases_smoothed)
    plt.title("World: 7-day smoothed new COVID-19 cases")
    plt.xlabel("Date"); plt.ylabel("Reported cases"); plt.grid(alpha=.25); plt.tight_layout()
    plt.savefig(OUT / "world_smoothed_cases.png", dpi=160); plt.close()
print(f"Rows: {len(df):,}; locations: {df.location.nunique()}; date range: {df.date.min().date()} to {df.date.max().date()}")
print(f"Outputs saved to: {OUT.resolve()}")
