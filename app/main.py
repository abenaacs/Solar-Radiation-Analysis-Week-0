import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import numpy as np
from datetime import datetime
from utils import (
    convert_timestamp_to_numeric,
    filter_data_by_time_range,
    create_time_series,
    create_wind_rose,
    create_cleaning_impact_plot,
    generate_correlation_matrix,
    generate_pair_plot,
    scatter_plot,
    plot_histogram,
    bubble_chart,
    clean_missing_values,
    remove_outliers,
)

# Constants
cleaning_col = "Cleaning"
mod_col = "ModA"
wind_dir_col = "WD"
wind_speed_col = "WS"
solar_temp_columns = ["GHI", "DNI", "DHI", "TModA", "TModB"]
wind_columns = ["WS", "WSgust", "WD", "GHI", "DNI"]


# Clear the cache for resource and memoized data
st.cache_data.clear()
st.cache_resource.clear()


# App title and description
st.set_page_config(page_title="Solar Radiation Dashboard", layout="wide")
st.title("Solar Radiation Analysis Dashboard")
st.write("Explore insights from solar radiation datasets across multiple regions.")

# Dataset options
datasets = {
    "Sierra Leone": "data/processed/sierraleone-cleaned.csv",
    "Benin": "data/processed/benin-cleaned.csv",
    "Togo": "data/processed/togo-cleaned.csv",
}

# Select dataset
selected_dataset = st.selectbox("Select a Dataset", options=list(datasets.keys()))
st.write(f"Currently selected dataset: {selected_dataset}")

# Load the selected dataset
df = pd.read_csv(datasets[selected_dataset])
df = clean_missing_values(df)
df = remove_outliers(df, columns=["GHI", "DNI", "DHI"])
st.write("Cleaned Data Preview:", df.head())
df = convert_timestamp_to_numeric(df)

# Convert pandas.Timestamp to Python datetime
min_time = df["Timestamp"].min().to_pydatetime()
max_time = df["Timestamp"].max().to_pydatetime()

# Time Range Slider
start_time, end_time = st.slider(
    "Select Time Range",
    min_value=min_time,
    max_value=max_time,
    value=(min_time, max_time),
    format="YYYY-MM-DD HH:mm",
)


df = filter_data_by_time_range(df, start_time, end_time)
st.write(f"Filtered Data ({start_time} to {end_time}):")


tab1, tab2, tab3 = st.tabs(["Overview", "Visualizations", "Raw Data"])

with tab1:
    st.write("Overview of Solar Radiation Insights")
    # Display dataset summary statistics
    st.write("#### Dataset Summary")
    st.write(
        "The dataset contains key solar radiation parameters recorded over time. Below are some basic statistics:"
    )
    st.write(df.describe())
    # Show statistical summary of numeric columns
    st.write(f"**Total Records:** {df.shape[0]} rows")
    st.write(f"**Number of Features:** {df.shape[1]} columns")

    # Display the date range of the data
    if "Timestamp" in df.columns:
        start_date = df["Timestamp"].min()
        end_date = df["Timestamp"].max()
        st.write(f"**Data Range:** {start_date} to {end_date}")

    # Key insights
    st.write("#### Key Insights")
    st.write(
        "- **Global Horizontal Irradiance (GHI)**: A measure of the total solar radiation on a horizontal surface."
    )
    st.write(
        "- **Direct Normal Irradiance (DNI)**: Measures direct sunlight at the surface."
    )
    st.write("- **Diffuse Horizontal Irradiance (DHI)**: Measures scattered sunlight.")
    st.write(
        "- The dataset includes cleaning impact and wind rose data, aiding in solar system performance analysis."
    )

with tab2:

    st.write("visualization goes here")
    if st.button("Generate Time-Series Plot"):
        st.write("Time-Series Plot:")
        fig = create_time_series(df)
        st.pyplot(fig)

    if st.button("Generate Cleaning_Impact Plot"):
        st.write("Cleaning-Impact Plot:")
        fig = create_cleaning_impact_plot(df, cleaning_col, mod_col)
        st.pyplot(fig)

    if st.button("Generate Wind-Rose Plot"):
        st.write("Wind-Rose Plot: ")
        fig = create_wind_rose(df, wind_dir_col, wind_speed_col)
        st.pyplot(fig)

    if st.button("Generate Correlation Matrix"):
        st.write("Correlation Matrix (Solar Radiation and Temperature):")
        fig = generate_correlation_matrix(df, solar_temp_columns)
        st.pyplot(fig)
    # Pair Plot for Solar Radiation and Temperature
    if st.button("Generate Pair Plot (Solar & Temp)"):
        st.write("Pair Plot (Solar Radiation and Temperature):")
        fig = generate_pair_plot(df, solar_temp_columns)
        st.pyplot(fig)

        # Correlation Analysis for Wind Conditions
    if st.button("Generate Wind Condition Correlation"):
        st.write("Correlation Matrix (Wind Conditions):")
        fig = generate_correlation_matrix(df, wind_columns)
        st.pyplot(fig)

        # Pair Plot for Wind and Solar Radiation
    if st.button("Generate Pair Plot (Wind & Solar)"):
        st.write("Pair Plot (Wind Conditions and Solar Radiation):")
        fig = generate_pair_plot(df, wind_columns)
        st.pyplot(fig)

    # Scatter Plots for Temperature Analysis
    if st.button("RH vs Temperature (TModA)"):
        st.write("Scatter Plot: RH vs Temperature (TModA)")
        fig = scatter_plot(df, x="RH", y="TModA", title="RH vs Temperature (TModA)")
        st.pyplot(fig)
    if st.button("RH vs Solar Radiation (GHI)"):
        st.write("Scatter Plot: RH vs Solar Radiation (GHI)")
        fig = scatter_plot(df, x="RH", y="GHI", title="RH vs Solar Radiation (GHI)")
        st.pyplot(fig)

        # Histograms
    if st.button("Histogram of GHI"):
        st.write("Histogram: GHI (Global Horizontal Irradiance)")
        fig = plot_histogram(df, column="GHI")
        st.pyplot(fig)

    if st.button("Histogram of WS"):
        st.write("Histogram: WS (Wind Speed)")
        fig = plot_histogram(df, column="WS")
        st.pyplot(fig)

    if st.button("Histogram of TModA"):
        st.write("Histogram: TModA (Module Temperature A)")
        fig = plot_histogram(df, column="TModA")
        st.pyplot(fig)
    if st.button("Generate Bubble Chart"):
        st.write("Bubble-Chart")
        fig = bubble_chart(
            df,
            x="GHI",
            y="Tamb",
            size="RH",
            color="WS",
            title="GHI vs Tamb vs WS (Size: RH)",
        )
        st.pyplot(fig)

    with tab3:
        st.write("Raw Data display.")
        st.write(df)

st.sidebar.title("Filters")
show_missing = st.sidebar.checkbox("Show Missing Values")
if show_missing:
    st.write(df.isnull().sum())
