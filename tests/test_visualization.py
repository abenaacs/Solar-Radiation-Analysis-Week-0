import unittest
from scripts.visualization import plot_time_series, plot_correlation_matrix
import pandas as pd
import matplotlib.pyplot as plt

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "Timestamp": pd.date_range("2023-01-01", periods=5, freq="D"),
            "GHI": [100, 200, 300, 400, 500],
            "DNI": [50, 100, 150, 200, 250],
        })

    def test_plot_time_series(self):
        try:
            plot_time_series(self.df)
            plt.close("all")
        except Exception as e:
            self.fail(f"plot_time_series failed: {e}")

    def test_plot_correlation_matrix(self):
        try:
            plot_correlation_matrix(self.df)
            plt.close("all")
        except Exception as e:
            self.fail(f"plot_correlation_matrix failed: {e}")

if __name__ == "__main__":
    unittest.main()
