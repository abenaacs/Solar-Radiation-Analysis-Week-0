# Solar Radiation Analysis Week 0

## Overview
The Solar Radiation Analysis Dashboard is an interactive web application built with Streamlit. It provides tools to explore and visualize solar radiation, temperature, and wind data. The dashboard offers features like time-series analysis, correlation matrices, bubble charts, and advanced data cleaning functionalities to help users derive meaningful insights from the data.

---

## Features
- **Data Cleaning**: Handles missing values and removes anomalies from critical variables like solar radiation (`GHI`, `DNI`, `DHI`).
- **Interactive Visualizations**: Includes time-series plots, correlation matrices, bubble charts, and more.
- **Data Filtering**: Filter datasets dynamically using a time range slider.
- **Deployment**: Hosted on Streamlit Community Cloud with CI/CD integration.

---

## Setup Instructions

### Prerequisites
- Python 3.9 or later
- A package manager (`pip` or `conda`)
- Git for version control

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abenaacs/Solar-Radiation-Analysis-Week-0.git
   cd solar-radiation-dashboard


**Set Up a Virtual Environment**:
    bash
    ```
    python -m venv env
    source env/bin/activate   # On Windows: .\env\Scripts\activate

**Install Dependencies**:
    bash
    ```
    pip install -r requirements.txt

**Run the App Locally**:
    bash
    ```
    streamlit run app/main.py

**Folder Structure**
    bash
    ```
    solar-radiation-dashboard/
    ├── app/                 # Main application scripts
    ├── notebooks/           # Jupyter notebooks for data exploration
    ├── scripts/             # Standalone scripts for data processing and visualization
    ├── tests/               # Unit tests
    ├── .github/workflows/   # CI/CD configuration
    ├── .streamlit/          # Streamlit configuration
    ├── requirements.txt     # Dependencies
    ├── README.md            # Project overview (this file)

**Contact**
Name: Abenezer Nigussie
Email: abenezernigussiecs@gmail.com
GitHub: abenaacs