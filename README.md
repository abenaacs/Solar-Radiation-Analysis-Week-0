
## **Solar Radiation Analysis Dashboard**

### **Overview**
The Solar Radiation Analysis Dashboard is an interactive web application built with Streamlit. It provides tools to explore and visualize solar radiation, temperature, and wind data. The dashboard offers features like time-series analysis, correlation matrices, bubble charts, and advanced data cleaning functionalities to help users derive meaningful insights from the data.

---

### **Features**
- **Data Cleaning**:
  - Automatically handles missing values and removes anomalies from critical variables like solar radiation (`GHI`, `DNI`, `DHI`).
- **Interactive Visualizations**:
  - Time-series plots for solar radiation and temperature data.
  - Correlation matrices to identify relationships between variables.
  - Bubble charts for exploring complex multi-variable relationships.
  - Histograms for frequency distribution of key metrics.
  - Scatter plots for relative humidity (`RH`) vs. temperature and solar radiation.
- **Data Filtering**:
  - Filter datasets dynamically using a time range slider.
  - Analyze missing values via the sidebar filter.
- **Deployment**:
  - Hosted on Streamlit Community Cloud with automated CI/CD for continuous integration and deployment.

---

### **Setup Instructions**

#### **Prerequisites**
- Python 3.9 or later
- A package manager (`pip` or `conda`)
- Git for version control

#### **Steps**
1. **Clone the Repository**:
   
   git clone https://github.com/abenaacs/solar-radiation-dashboard.git
   cd solar-radiation-dashboard
   

2. **Set Up a Virtual Environment**:
   
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   

3. **Install Dependencies**:
   
   pip install -r requirements.txt
   

4. **Run the App Locally**:
   
   streamlit run app/main.py
   

---

### **Usage Instructions**

1. **Select a Dataset**:
   - Choose one of the available datasets (e.g., Sierra Leone, Benin, or Togo) from the dropdown menu.

2. **Explore Data**:
   - Navigate through the tabs:
     - **Overview**: Displays a high-level summary of the data.
     - **Visualizations**: Offers buttons to generate various interactive plots.
     - **Raw Data**: Shows the entire dataset for inspection.

3. **Visualizations**:
   - Use the **"Visualizations" tab** to generate:
     - Time-series plots
     - Correlation matrices
     - Scatter plots
     - Bubble charts
     - Histograms

4. **Filter Data**:
   - Use the time range slider to filter data dynamically.
   - Apply sidebar filters to analyze missing values.

5. **Deploy**:
   - The app is hosted on Streamlit Community Cloud and can be accessed via [App Link](https://your-app-link.streamlit.app).

---

### **Folder Structure**

solar-radiation-dashboard/
├── app/
│   ├── main.py               # Main Streamlit app script
│   ├── utils.py              # Data cleaning and utility functions
├── scripts/
│   ├── visualization.py      # Functions for generating visualizations
│   ├── cleaning.py           # Functions for handling data cleaning (if separated)
├── data/
│   ├── raw/                  # Raw datasets
│   ├── processed/            # Processed datasets
├── tests/
│   ├── test_cleaning.py      # Unit tests for cleaning functions
│   ├── test_visualization.py # Unit tests for visualization functions
├── .github/
│   └── workflows/
│       ├── ci-cd.yml         # GitHub Actions CI/CD pipeline configuration
├── requirements.txt          # Dependencies for the project
├── README.md                 # Project documentation


---

### **CI/CD Pipeline**
The project includes a fully configured CI/CD pipeline using GitHub Actions:

1. **Lint and Test**:
   - Automatically checks the codebase for syntax issues and style inconsistencies using `flake8`.
   - Runs unit tests using Python’s built-in `unittest`.

2. **Deployment**:
   - Automatically deploys the app to Streamlit Community Cloud when changes are pushed to the `main` branch.

#### **Pipeline Configuration**
The pipeline is defined in `.github/workflows/ci-cd.yml`:
- Triggers:
  - On every push or pull request to the `main` branch.
- Jobs:
  - **Linting and Testing**: Ensures code quality.
  - **Deployment**: Deploys the app to Streamlit Community Cloud.

---

### **Data Cleaning Details**
1. **Missing Values**:
   - Columns with all values missing (e.g., `Comments`) are dropped.
   - Missing numeric values are filled with the column mean.

2. **Anomalies**:
   - Outliers in critical variables (`GHI`, `DNI`, `DHI`) are identified using Z-scores and removed.

---

### **Technologies Used**
- **Streamlit**: Interactive web app framework.
- **Pandas**: Data manipulation and cleaning.
- **Seaborn**: Advanced visualizations.
- **Matplotlib**: Core plotting library.
- **GitHub Actions**: CI/CD for automated testing and deployment.

---

### **Testing**
The project includes unit tests to ensure reliability:
- **Data Cleaning**:
  - Tests for handling missing values and outlier removal.
- **Visualizations**:
  - Placeholder tests for time-series plots, correlation matrices, and other visualizations.

Run the test suite using:

python -m unittest discover -s tests


---

### **Future Enhancements**
- Add advanced filtering options for scatter plots and bubble charts.
- Incorporate real-time data fetching for more dynamic analysis.
- Add export functionality for processed datasets and visualizations.

---

### **Contributing**
We welcome contributions to improve the dashboard! To contribute:
1. Fork the repository.
2. Create a new branch:
   
   git checkout -b feature-name
   
3. Commit your changes:
   git commit -m "Add new feature"

4. Push the changes and open a pull request:
   
   git push origin feature-name
   

---

### **Acknowledgements**
- **Datasets**: Sourced from [Specify Dataset Source Here].
- **Program**: Developed as part of the 10 Academy AI Mastery Program.

---

### **Contact**
For inquiries or feedback, contact:
- **Name**: Abenezer Nigussie
- **Email**: abenezernigussiecs@gmail.com
- **GitHub**: [abenaacs](https://github.com/abenaacs)

---