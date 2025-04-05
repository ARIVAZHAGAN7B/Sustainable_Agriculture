from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import AdvisorAgent, MarketAgent
from pydantic import BaseModel

app = FastAPI()

# ✅ Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # adjust for your frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Define request schema
class PredictionRequest(BaseModel):
    soil_pH: float
    soil_moisture: float
    temp: float
    rainfall: float
    fertilizer: float
    pesticide: float
    crop_type: int
    product: int
    demand_index: float
    supply_index: float
    competitor_price: float
    economic_factor: float
    weather_impact: float
    season_factor: float
    consumer_trend: float


@app.get("/")
def start():
    return "Hello world"
@app.post("/predict")
def predict(request: PredictionRequest):
    advisor = AdvisorAgent()
    market = MarketAgent()

    crop_yield = advisor.recommend_crop(
        soil_pH=request.soil_pH,
        soil_moisture=request.soil_moisture,
        temp=request.temp,
        rainfall=request.rainfall,
        fertilizer=request.fertilizer,
        pesticide=request.pesticide,
        crop_type=request.crop_type
    )

    market_price = market.predict_price(
        product=request.product,
        demand_index=request.demand_index,
        supply_index=request.supply_index,
        competitor_price=request.competitor_price,
        economic_factor=request.economic_factor,
        weather_impact=request.weather_impact,
        season_factor=request.season_factor,
        consumer_trend=request.consumer_trend
    )

    return {
        "crop_yield": crop_yield,
        "market_price": market_price
    }
