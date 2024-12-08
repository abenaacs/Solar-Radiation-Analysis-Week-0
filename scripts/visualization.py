import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from windrose import WindroseAxes

def plot_time_series(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Ensure Timestamp is datetime
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['GHI'], label='GHI')
    plt.plot(df['Timestamp'], df['DNI'], label='DNI')
    plt.plot(df['Timestamp'], df['DHI'], label='DHI')
    plt.title("Solar Radiation Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Radiation (W/m²)")
    plt.legend()
    plt.grid()
    plt.show()

def plot_correlation_matrix(df, columns):
    """Plots a correlation heatmap for the dataset."""
    if 'Timestamp' in df.columns:
        df['timestamp_numeric'] = pd.to_datetime(df['Timestamp'], errors='coerce').astype('int64') // 10**9
    # Select only numeric columns
    numeric_data = df.select_dtypes(include=[np.number])
    
    if numeric_data.empty:
        print(f"No numeric data in dataset to compute correlations.")
        return
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_data[columns].corr(), annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
    plt.title("Correlation Matrix")
    plt.show()

def plot_cleaning_impact(df):
    df_cleaning = df[df['Cleaning'] == 1]
    df_no_cleaning = df[df['Cleaning'] == 0]
    plt.boxplot([df_cleaning['ModA'], df_no_cleaning['ModA']], labels=['Cleaned', 'Not Cleaned'])
    plt.title("Impact of Cleaning on ModA")
    plt.ylabel("ModA (W/m²)")
    plt.show()

def plot_wind_rose(df):
    ax = WindroseAxes.from_ax()
    ax.bar(df['WD'], df['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.title("Wind Rose")
    plt.show()


def generate_pair_plot(df, columns):
    sns.pairplot(df[columns], diag_kind="kde", corner=True)
    plt.title("Pair Plot (Scatter Plot Matrix)")
    plt.show()

def scatter_plot(df, x, y, title="Scatter Plot"):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_histogram(df, column, bins=20):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x=column, bins=bins, kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def bubble_chart(df, x, y, size, color=None, title="Bubble Chart"):
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(
        x=df[x],
        y=df[y],
        s=df[size] * 100,  # Scale bubble size
        c=df[color] if color else None,
        alpha=0.6,
        cmap="viridis"
    )
    plt.colorbar(scatter, label=color) if color else None
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
