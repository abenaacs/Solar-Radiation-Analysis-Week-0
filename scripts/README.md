
---
### Scripts for Solar Radiation Analysis


## Overview
The `scripts` directory contains standalone Python scripts for specific tasks such as data cleaning, processing, and visualization. These scripts support the main application by modularizing complex workflows.

---

## Contents
- **`visualization.py`**:
  - Functions for generating interactive visualizations (time-series plots, scatter plots, bubble charts, etc.).
  - Used by the Streamlit application for dynamic rendering.

- **`cleaning.py`**:
  - Functions for data cleaning, including handling missing values and removing outliers.
  - Ensures data quality for accurate analysis.

---

## Usage
1. **Import Functions**:
   - Scripts can be imported into other Python files:
     ```python
     from scripts.cleaning import clean_data
     from scripts.visualization import plot_time_series
     ```

2. **Run Scripts Individually**:
   - Each script can also be executed as a standalone file for debugging or testing:
     ```bash
     python scripts/cleaning.py
     ```

---
