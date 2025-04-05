import random

class WeatherAgent:
    def get_weather_forecast(self):
        """Simulates weather forecast data."""
        return {
            "temperature": round(random.uniform(15, 35), 2),
            "rainfall": round(random.uniform(50, 300), 2),
            "humidity": round(random.uniform(40, 90), 2),
        }
