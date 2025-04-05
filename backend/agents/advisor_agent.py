import joblib
import pandas as pd

class AdvisorAgent:
    def __init__(self, model_path="crop_yield_model.pkl"):
        self.model = joblib.load(model_path)

    def recommend_crop(self, soil_pH, soil_moisture, temp, rainfall, fertilizer, pesticide, crop_type):
        """Predicts optimal crop yield based on input parameters."""
        data = pd.DataFrame([{
            'Soil_pH': soil_pH,
            'Soil_Moisture': soil_moisture,
            'Temperature_C': temp,
            'Rainfall_mm': rainfall,
            'Crop_Type': crop_type,
            'Fertilizer_Usage_kg': fertilizer,
            'Pesticide_Usage_kg': pesticide
        }])
        yield_prediction = self.model.predict(data)[0]
        return f"Recommended crop should yield approximately {yield_prediction:.2f} tons."
