# Health and Safety Data Analysis

Health and Safety Data Analysis is a Python project that examines workplace incident records from Ireland between 2017 and 2021. It loads a CSV dataset, prepares the data for analysis, counts incidents by type, and creates a visualization to help compare the frequency of different incident categories.

## Features

The project currently supports:

- **CSV data loading** — Reads workplace incident records into a Pandas DataFrame.
- **Data cleaning** — Removes leading and trailing spaces from column names and excludes rows with missing incident types.
- **Incident analysis** — Counts records in each incident category using Pandas.
- **Data preview** — Displays the first 20 records to help inspect the loaded dataset.
- **Data visualization** — Generates a bar chart of incident counts using Matplotlib and Seaborn.
- **Chart labels** — Displays the count for each category and uses a logarithmic y-axis to make categories with different frequencies easier to compare.

## Project Structure

```text
health_safety_data_analysis/
│
├── data/
│   └── government_of_Ireland_workplace_incidents_2017-2021.csv
│
├── src/
│   ├── main.py
│   ├── workplace_incident_analysis.py
│   └── visual.py
│
├── requirements.txt
└── README.md
```

## How It Works

The application follows a simple data analysis pipeline:

```text
Workplace Incident CSV
         │
         ▼
      Load Data
         │
         ▼
      Clean Data
         │
         ▼
  Count Incident Types
         │
         ├───────────────┐
         ▼               ▼
  Print Counts      Create Bar Chart
                         │
                         ▼
                   Display Chart
```

The program loads the incident dataset, standardizes the column names, and excludes records without an `Incident Type`. It then counts how often each incident type appears, prints those counts in the terminal, and displays a labeled bar chart.

## Dataset

The included CSV contains **45,897 workplace incident records** spanning **2017–2021**. Its fields include age, gender, industry sector, incident type, employment status, year, county, and incident trigger.

The current analysis focuses on the **Incident Type** column. Other fields are available in the dataset but are not yet used for separate breakdowns in the application.

## Running the Application

### 1. Set up Python

Install Python and, from the project directory, create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

The main libraries used by the application are **Pandas**, **Matplotlib**, and **Seaborn**.

### 3. Run the program

Run the following command **from the project root directory**, so the relative dataset path resolves correctly:

```bash
python src/main.py
```

The program prints a preview of the dataset, displays the incident counts in the terminal, and opens a window with the bar chart.

## Example Output

The incident counts for the included dataset are:

```text
Incident Counts:
Non-fatal injury        44148
Dangerous Occurrence     1451
Fatality                  227
Non-work related           71
```

The corresponding bar chart is titled **Workplace incidents by type**. Each bar represents an incident category, with its count displayed above it. The y-axis uses a logarithmic scale because the categories vary substantially in frequency.

## Design

The project separates data processing, visualization, and program execution into three Python modules. Each module has a specific responsibility, making the analysis easier to follow and extend.

### Main Application

`src/main.py` coordinates the workflow: it loads the dataset, calls the cleaning and analysis functions, prints results, and passes the incident counts to the plotting function.

### Data Analysis

`src/workplace_incident_analysis.py` contains three functions:

- **`load_data()`** — Loads the CSV file into a Pandas DataFrame.
- **`clean_data()`** — Strips whitespace from column names and drops rows with missing `Incident Type` values.
- **`incident_count()`** — Uses `value_counts()` to calculate the number of records in each incident category.

### Data Visualization

`src/visual.py` uses Seaborn and Matplotlib to create the incident-type bar chart. The chart includes category labels, numeric counts, a title, grid styling, and a logarithmic y-axis.

## Current Scope

The implemented analysis summarizes **incidents by type**. Breakdown charts by year, county, industry sector, or trigger; interactive dashboards; and automated report exports are **not part of the current implementation**.
