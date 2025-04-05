import joblib
import pandas as pd

class MarketAgent:
    def __init__(self, model_path="market_price_model.pkl"):
        self.model = joblib.load(model_path)

    def predict_price(self, product, demand_index, supply_index, competitor_price,
                      economic_factor, weather_impact, season_factor, consumer_trend):
        """Predicts market price per ton for a given crop."""
        data = pd.DataFrame([{
            'Product': product,
            'Demand_Index': demand_index,
            'Supply_Index': supply_index,
            'Competitor_Price_per_ton': competitor_price,
            'Economic_Indicator': economic_factor,
            'Weather_Impact_Score': weather_impact,
            'Seasonal_Factor': season_factor,
            'Consumer_Trend_Index': consumer_trend
        }])
        price_prediction = self.model.predict(data)[0]
        return f"Predicted market price per ton: ₹{price_prediction:.2f}"
