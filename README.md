# COVID-19 Global Impact Dashboard

A beginner-friendly data analytics project exploring historical reported COVID-19 trends using the **Our World in Data (OWID)** dataset.

## Project contents
- `data/covid_dashboard_data.csv` — repository-friendly extract for World, available continent aggregates, and 12 selected countries.
- `python/analyze_covid.py` — reproducible cleaning and chart-generation script.
- `excel/COVID19_Global_Impact_Analysis.xlsx` — analysis workbook with data, country latest values, and World summary.
- `charts/` — generated figures used in the report.
- `report/COVID19_Global_Impact_Executive_Report.pdf` — executive report.
- `powerbi/` and `tableau/` — folders for adding your finished `.pbix` / Tableau workbook and screenshots.

## Dataset
Source documentation: https://github.com/owid/covid-19-data/tree/master/public/data

The original uploaded CSV has approximately 350,085 rows across 255 locations and 67 source columns. To avoid GitHub's browser upload size limit, this repository contains a filtered extract for the World aggregate, available continent aggregates, and these selected countries: United States, India, Brazil, United Kingdom, France, Germany, Italy, Japan, Canada, Australia, South Africa, Indonesia. The extract covers 2020-01-03 through 2023-10-23. It is not the complete source dataset.

## Run the Python workflow
Python 3.10+ recommended.

```bash
pip install -r requirements.txt
python python/analyze_covid.py data/covid_dashboard_data.csv
```

The script creates an `output/` folder containing cleaned data and a global trend chart.

## Power BI dashboard plan
1. Open Power BI Desktop and select **Home → Get data → Text/CSV**.
2. Import `data/covid_dashboard_data.csv`.
3. Set `date` to Date and measure columns to numeric types.
4. Add a World line chart for `new_cases_smoothed` over `date`, filtered to `location = World`.
5. Add a country bar chart using `total_cases_per_million` for one comparable date.
6. Add slicers for `continent`, `location`, and `date`.
7. Save your work as `powerbi/COVID19_Global_Impact.pbix` and upload it only after you have created and checked it.

## Important interpretation notes
- Do not sum cumulative totals across every date.
- The last available non-missing date can differ by location and metric.
- Missing values are not automatically zero.
- Per-million measures help population comparisons but do not remove differences in testing, reporting, and case definitions.
- The included workbook/report are historical analysis, not medical advice or live surveillance.

## Tools
Python, Pandas, Matplotlib, Microsoft Excel, and Power BI or Tableau for the interactive dashboard.

## Project status
The Python, Excel, chart, and PDF-report assets are included. Add your final Power BI/Tableau file and a screenshot after completing the interactive dashboard.

