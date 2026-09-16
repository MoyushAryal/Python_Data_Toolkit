# Python Data Toolkit

A small Python data-cleaning and analysis toolkit built to process messy CSV data and produce useful statistics.

## How It Works

The application follows a simple pipeline:

```text
CSV Data
   ↓
Load Records
   ↓
Clean Data
   ↓
Analyze Data
   ↓
Generate Report
```

### 1. Loading Data

The `Dataset` class reads the CSV file using Python's built-in `csv` module and converts each row into a `Record` object.

The number of rows loaded is also tracked for reporting.

### 2. Cleaning Data

The cleaning process applies the following rules:

* **Completely blank rows** → removed.
* **Age**

  * Numeric ages are converted to `int`.
  * Ages written as words are converted using the word-to-number dictionary.
  * Invalid ages are removed.
* **ID**

  * IDs are converted to `int`.
  * Invalid IDs are removed.
  * Duplicate IDs are removed, keeping the first occurrence.
* **Name**

  * Missing names are replaced with `"Unknown"`.
* **City**

  * Missing cities are replaced with `"Unknown"`.
* **Score**

  * Valid scores are converted to `float`.
  * Missing or invalid scores are replaced with the mean of the valid scores.

The toolkit also keeps counters for the different types of cleaning operations, such as invalid ages, duplicate IDs, missing scores, and missing names.

### 3. Analysis

After cleaning, the toolkit can calculate:

* Average score
* Number of people per city
* Oldest person
* Youngest person

A `stream()` method also uses `yield` to provide cleaned records one at a time.

### 4. Timing

Analysis methods use a `log_time` decorator to measure and display how long each method takes to execute.

### 5. Report

The reporting module combines the cleaning information and analysis results into a terminal report showing:

* Rows loaded
* Rows dropped
* Reasons for dropped rows
* Data that was fixed or imputed
* Key statistics

## Project Structure

```text
finalToolkit/
│
├── main.py
├── data/
│   └── messy_people (1).csv
│
├── logic/
│   ├── models.py
│   └── dataset.py
│
├── tools/
│   ├── decorators.py
│   └── word_to_number.py
│
└── Report/
    └── report.py
```

`main.py` acts as the entry point and connects the different parts of the toolkit.

The project is organized into separate modules so that data logic, reusable tools, input data, and reporting are kept independent and easier to maintain.
