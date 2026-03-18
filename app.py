from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

# Define input format
class HouseData(BaseModel):
    year: int
    month: int
    median_list_price: float
    median_ppsf: float
    homes_sold: int
    inventory: int
    lat: float
    lng: float
    city_encoded: int

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running 🚀"}

@app.post("/predict")
def get_prediction(data: HouseData):
    prediction = predict(data.dict())
    return {"predicted_price": prediction}