import unittest
import pandas as pd
from app.utils import clean_missing_values, remove_outliers

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        # Sample dataset
        self.df = pd.DataFrame({
            "GHI": [100, 200, None, 400, float("inf")],
            "DNI": [None, 150, 250, 350, 450],
            "Comments": [None, None, None, None, None],
        })

    def test_clean_missing_values(self):
        cleaned_df = clean_missing_values(self.df)
        self.assertFalse(cleaned_df.isnull().any().any(), "There are still missing values after cleaning")
        self.assertNotIn("Comments", cleaned_df.columns, "Comments column should be dropped")

    def test_remove_outliers(self):
        cleaned_df = clean_missing_values(self.df)
        outlier_removed_df = remove_outliers(cleaned_df, columns=["GHI", "DNI"])
        self.assertTrue((outlier_removed_df["GHI"] < float("inf")).all(), "Outliers not removed correctly")

if __name__ == "__main__":
    unittest.main()
