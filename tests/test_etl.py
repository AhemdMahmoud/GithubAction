import os
import csv

# Update path to match where ETL writes the CSV
CSV_PATH = "dbt_project/seeds/output_csv.csv"

def test_output_file():
    assert os.path.exists(CSV_PATH)

def test_csv_content():
    with open(CSV_PATH, newline="") as f:
        reader = list(csv.DictReader(f))
        assert reader[0]["name"] == "Ali"
        assert reader[1]["age"] == "30"