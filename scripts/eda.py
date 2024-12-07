import pandas as pd
import matplotlib.pyplot as plt
from cleaning import handle_missing_values, detect_outliers
from visualization import plot_time_series, plot_correlation_matrix, plot_cleaning_impact, plot_wind_rose, generate_pair_plot, scatter_plot, plot_histogram, bubble_chart
# Load the dataset


# List of datasets and their names
datasets = [
    {"name": "sierraleone", "path": "data/raw/sierraleone-bumbuna.csv"},
    {"name": "benin", "path": "data/raw/benin-malanville.csv"},
    {"name": "togo", "path": "data/raw/togo-dapaong_qc.csv"},
]
solar_temp_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
wind_columns = ['WS', 'WSgust', 'WD', 'GHI', 'DNI']

for dataset in datasets:
    print(f"Processing dataset: {dataset['name']}")

    # Load the dataset
    try:
        df = pd.read_csv(dataset["path"])
        # Data Cleaning

        df = handle_missing_values(df)
        df = detect_outliers(df)

        # Save cleaned dataset
        output_path = f"data/processed/{dataset['name']}-cleaned.csv"
       
        df.to_csv(output_path, index=False) 

        # Visualizations
        plot_time_series(df)
        plot_correlation_matrix(df,solar_temp_columns )
        plot_correlation_matrix(df, wind_columns)
        plot_cleaning_impact(df)
        plot_wind_rose(df)
        generate_pair_plot(df, solar_temp_columns)
        generate_pair_plot(df, wind_columns)
        scatter_plot(df, x="RH", y="GHI", title="RH vs Solar Radiation (GHI)")
        plot_histogram(df, column="GHI")
        plot_histogram(df, column="WS")
        plot_histogram(df, column="TModA")
        bubble_chart(df,x="GHI", y="Tamb", size="RH", color="WS", title="GHI vs Tamb vs WS (Size: RH)")


        print(f"Finished processing {dataset['name']}")

    except Exception as e:
        print(f"Error processing dataset {dataset['name']}: {e}")
        continue

print("All datasets processed successfully!")


combined_df = pd.concat([pd.read_csv(f"data/processed/{d['name']}-cleaned.csv") for d in datasets])
combined_df.to_csv("data/processed/combined-cleaned.csv", index=False)

