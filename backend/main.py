from agents.farmer_agent import FarmerAgent
from agents.advisor_agent import AdvisorAgent
from agents.market_agent import MarketAgent
from agents.weather_agent import WeatherAgent

def run_prediction(inputs):
    farmer = FarmerAgent()
    farmer.collect_data(land_size=inputs["land_size"],
                        crop_preference=inputs["crop_preference"],
                        financial_budget=inputs["financial_budget"])

    # Simulate weather
    weather = WeatherAgent()
    forecast = weather.get_weather_forecast()

    # Advisor
    advisor = AdvisorAgent()
    crop_result = advisor.recommend_crop(
        soil_pH=inputs["soil_pH"],
        soil_moisture=inputs["soil_moisture"],
        temp=forecast["temperature"],
        rainfall=forecast["rainfall"],
        fertilizer=inputs["fertilizer"],
        pesticide=inputs["pesticide"],
        crop_type=inputs["crop_type"]
    )

    # Market
    market = MarketAgent()
    price_result = market.predict_price(
        product=inputs["product"],
        demand_index=inputs["demand_index"],
        supply_index=inputs["supply_index"],
        competitor_price=inputs["competitor_price"],
        economic_factor=inputs["economic_factor"],
        weather_impact=inputs["weather_impact"],
        season_factor=inputs["season_factor"],
        consumer_trend=inputs["consumer_trend"]
    )

    return {
        "crop_yield": crop_result,
        "market_price": price_result,
        "weather_used": forecast
    }
