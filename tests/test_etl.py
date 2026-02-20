import os
import csv
import pytest

def test_output_file():
    assert os.path.exists("output.csv")

def test_csv_content():
    with open("output.csv", newline="") as f:
        reader = list(csv.DictReader(f))
        assert reader[0]["name"] == "Ali"
        assert reader[1]["age"] == "30"