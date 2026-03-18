import pickle
import pandas as pd
import os

# Get base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model + columns
model_path = os.path.join(BASE_DIR, "artifacts", "model.pkl")
columns_path = os.path.join(BASE_DIR, "artifacts", "columns.pkl")

model = pickle.load(open(model_path, "rb"))
columns = pickle.load(open(columns_path, "rb"))

def predict(data: dict):

    df = pd.DataFrame([data])

    # Ensure same columns
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return float(prediction)