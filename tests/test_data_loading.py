import pandas as pd

def test_load_benin_data():
    try:
        df = pd.read_csv("../data/benin-malanville.csv")
        assert not df.empty, "Dataset is empty"
    except Exception as e:
        assert False, f"Error loading Benin data: {e}"

def test_load_sierraleone_data():
    try:
        df = pd.read_csv("../data/sierraleone-bumbuna.csv")
        assert not df.empty, "Dataset is empty"
    except Exception as e:
        assert False, f"Error loading Sierra Leone data: {e}"

def test_load_togo_data():
    try:
        df = pd.read_csv("../data/togo-dapaong_qc.csv")
        assert not df.empty, "Dataset is empty"
    except Exception as e:
        assert False, f"Error loading Togo data: {e}"


