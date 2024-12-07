import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from windrose import WindroseAxes
import numpy as np
from scipy.stats import zscore

# Convert 'Timestamp' to numeric (days since start date)
def convert_timestamp_to_numeric(df):
    """
    Converts 'Timestamp' column to numeric (days since start date).
    """
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Timestamp_numeric'] = (df['Timestamp'] - df['Timestamp'].min()).dt.total_seconds() / (24 * 60 * 60)  # Convert to days
    return df

# Filter data based on timestamp range
def filter_data_by_time_range(df, start_time, end_time):
    """
    Filters the dataset to include only the rows where the 'Timestamp' is within the selected range.
    """
    filtered_df = df[(df['Timestamp'] >= start_time) & (df['Timestamp'] <= end_time)]
    return filtered_df

def create_time_series(df):
    """
    Create a Time Series Plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["Timestamp"], df["GHI"], label="Global Horizontal Irradiance (GHI)")
    ax.plot(df['Timestamp'], df['DNI'], label='DNI')
    ax.plot(df['Timestamp'], df['DHI'], label='DHI')
    ax.set_title("Solar Radiation Over Time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Radiation (W/m²)")
    ax.legend()
    return fig

def create_wind_rose(df, wind_dir_col, wind_speed_col):
    """
    Create a Wind Rose plot.
    """
    if wind_dir_col in df.columns and wind_speed_col in df.columns:
        fig = plt.figure(figsize=(6, 6))
        ax = WindroseAxes.from_ax(fig=fig)
        ax.bar(df[wind_dir_col], df[wind_speed_col], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        ax.set_title("Wind Rose")
        return fig
    else:
        raise ValueError(f"Required columns ({wind_dir_col}, {wind_speed_col}) are missing in the dataset.")


def create_cleaning_impact_plot(df, cleaning_col, mod_col):
    """
    Create a boxplot to visualize the impact of cleaning. Boxplot figure.
    """
    if cleaning_col in df.columns and mod_col in df.columns:
        df_cleaning = df[df[cleaning_col] == 1]
        df_no_cleaning = df[df[cleaning_col] == 0]
        fig, ax = plt.subplots()
        ax.boxplot([df_cleaning[mod_col], df_no_cleaning[mod_col]], labels=['Cleaned', 'Not Cleaned'])
        ax.set_title("Impact of Cleaning")
        ax.set_ylabel(mod_col)
        return fig
    else:
        raise ValueError(f"Required columns ({cleaning_col}, {mod_col}) are missing in the dataset.")


# Generate correlation matrix
def generate_correlation_matrix(df, columns):
    """
    Generates and returns the correlation matrix for the numeric columns.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    numeric_data = df.select_dtypes(include=[np.number])
    
    if numeric_data.empty:
        st.write("No numeric data in the dataset to compute correlations.")
    else:
        sns.heatmap(numeric_data[columns].corr(), annot=True, cmap="coolwarm", fmt=".2f", cbar=True, ax=ax)
        ax.set_title("Correlation Matrix")
        ax.tight_layout()
    return fig

def generate_pair_plot(df, columns):
    """
    Generates a pair plot (scatter plot matrix) for the specified columns.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.pairplot(df[columns], diag_kind="kde", corner=True)
    ax.title("Pair Plot (Scatter Plot Matrix)")
    ax.show()
    return fig

def scatter_plot(df, x, y, title="Scatter Plot"):
    """
    Creates a scatter plot for two variables.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y)
    ax.title(title)
    ax.xlabel(x)
    ax.ylabel(y)
    ax.grid(True)
    ax.tight_layout()
    return fig


def plot_histogram(df, column, bins=20):
    """
    Creates a histogram for a single variable.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.figure(figsize=(8, 6))
    sns.histplot(data=df, x=column, bins=bins, kde=True)
    ax.title(f"Histogram of {column}")
    ax.xlabel(column)
    ax.ylabel("Frequency")
    ax.grid(True)
    ax.tight_layout()
    return fig


def bubble_chart(df, x, y, size, color=None, title="Bubble Chart"):
    """
    Creates a bubble chart for exploring relationships between variables.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(
        x=df[x],
        y=df[y],
        s=df[size] * 100,  # Scale bubble size
        c=df[color] if color else None,
        alpha=0.6,
        cmap="viridis"
    )
    ax.colorbar(scatter, label=color) if color else None
    ax.title(title)
    ax.xlabel(x)
    ax.ylabel(y)
    ax.grid(True)
    ax.tight_layout()
    return fig


def clean_missing_values(df):
    """
    Handles missing values in the dataset.
    - Drops entirely null columns (like 'Comments').
    """
    # Ensure df is a copy to avoid SettingWithCopyWarning
    df = df.copy()

    # Drop columns entirely null
    df = df.dropna(axis=1, how="all")

    # Fill numeric columns with mean
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    for col in numeric_cols:
        df.loc[:, col] = df[col].fillna(df[col].mean())
    return df


def remove_outliers(df, columns, z_threshold=3):
    """
    Removes rows where the specified columns have outliers based on Z-scores.
    """
    z_scores = zscore(df[columns])
    mask = (abs(z_scores) < z_threshold).all(axis=1)
    return df[mask]
