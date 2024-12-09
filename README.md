# **Solar Radiation Analysis - Week 0**

## **Overview**
The **Solar Radiation Analysis** project, developed by **Abenezer Nigussie**, is a tool for exploring and analyzing solar radiation, temperature, and wind data. It includes:  
1. **Standalone Python scripts** for automated data cleaning, processing, and visualization.  
2. An **interactive Streamlit dashboard** for dynamic data exploration.  

Deployed link: [Solar Radiation Dashboard](https://abenaacs-solar-radiation-analysis-week-0-appmain-mqrye6.streamlit.app/)
---
## **Features**
1. **Data Cleaning**:
   - Handles missing values (`GHI`, `DNI`, `DHI`) by filling numeric columns with their means.
   - Removes anomalies using Z-score thresholds.  
2. **Data Analysis**:
   - Batch processes multiple datasets, saving cleaned versions for reuse.
   - Provides statistical and graphical insights through Python scripts.  
3. **Interactive Visualizations** (via Streamlit):
   - Time-series plots, correlation matrices, bubble charts, and histograms.
   - Dynamic data filtering using time sliders.  
---
## **Setup Instructions**

### **Prerequisites**
- Python 3.9 or later  
- Git and a package manager (`pip` or `conda`)  

### **Steps**
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/abenaacs/Solar-Radiation-Analysis-Week-0.git
   cd Solar-Radiation-Analysis-Week-0
   ```
2. **Set Up a Virtual Environment**:  
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```
3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Locally**:
   - **Python Script**:
     ```bash
     python scripts/eda.py
     ```
     Outputs:
     - Cleaned datasets saved in `data/processed/`.
     - Visualizations saved in the `output/` directory.
   - **Streamlit Dashboard**:
     ```bash
     streamlit run app/main.py
     ```
---

## **How to Use the Project**

### **Standalone Python Scripts**
The `scripts/eda.py` script cleans datasets and generates visualizations.  

#### Example:
```python
from scripts.cleaning import clean_missing_values
from scripts.visualization import plot_time_series

# Load and clean dataset
df = pd.read_csv("data/raw/sierraleone.csv")
df_cleaned = clean_missing_values(df)

# Generate a time-series plot
plot_time_series(df_cleaned)
```

### **Streamlit Dashboard**
1. Access the dashboard:  
   [Solar Radiation Dashboard](https://abenaacs-solar-radiation-analysis-week-0-appmain-mqrye6.streamlit.app/)  
2. Select a dataset (e.g., Sierra Leone, Benin, Togo).  
3. Use interactive features like visualizations and timestamp filtering.

---

## **CI/CD Pipelines**

### **Overview**
The project includes a **CI/CD pipeline** using GitHub Actions, ensuring automated testing and deployment.  

### **Pipeline Workflow**
1. **Trigger Conditions**:
   - Push to the `main` branch.
   - Pull requests targeting `main`.  
2. **Pipeline Steps**:
   - **Lint and Test**:
     - Lints the code with `flake8`.
     - Runs unit tests with Python’s `unittest`.  
   - **Deploy**:
     - Deploys the Streamlit app to Streamlit Community Cloud.  

### **Configuration**
The pipeline is defined in `.github/workflows/ci-cd.yml`. Below is a simplified version:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Lint code
        run: flake8 app scripts tests
      - name: Run tests
        run: python -m unittest discover -s tests

  deploy:
    needs: lint-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy Streamlit App
        run: streamlit deploy app/main.py
        env:
          STREAMLIT_AUTH_TOKEN: ${{ secrets.STREAMLIT_AUTH_TOKEN }}
```

### **Local and Automated Deployment**
- **Local Deployment**:
  ```bash
  streamlit run app/main.py
  ```
- **Automated Deployment**:
  Pushing changes to the `main` branch triggers the CI/CD pipeline, which:
  1. Lints and tests the code.
  2. Deploys the app to Streamlit Community Cloud.  

---

## **Folder Structure**

```bash
solar-radiation-dashboard/
├── app/                 # Streamlit app
├── scripts/             # Data processing and visualization scripts
├── tests/               # Unit tests
├── data/                # Raw and processed datasets
├── .github/workflows/   # CI/CD configuration
├── .streamlit/          # Streamlit settings
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

---

## **Contact**

- **Name**: Abenezer Nigussie  
- **Email**: [abenezernigussiecs@gmail.com](mailto:abenezernigussiecs@gmail.com)  
- **GitHub**: [abenaacs](https://github.com/abenaacs)  
