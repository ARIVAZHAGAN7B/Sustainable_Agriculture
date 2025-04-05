import React, { useState } from 'react';

const FarmPredictor = () => {
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    try {
      const response = await fetch("https://farmiq-oj99.onrender.com/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          soil_pH: 10.5,
          soil_moisture: 20.0,
          temp: 30.2,
          rainfall: 120.5,
          fertilizer: 50.0,
          pesticide: 10.0,
          crop_type: 3,
          product: 3,
          demand_index: 70.0,
          supply_index: 50.0,
          competitor_price: 300.0,
          economic_factor: 1.2,
          weather_impact: 1.0,
          season_factor: 1.0,
          consumer_trend: 65.0
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Prediction failed:", error);
    }
  };

  return (
    <div>
      <button onClick={handlePredict}>Get Predictions</button>
      {result && (
        <div>
          <p><strong>Crop Yield:</strong> {result.crop_yield}</p>
          <p><strong>Market Price:</strong> ₹{result.market_price}</p>
        </div>
      )}
    </div>
  );
};

export default FarmPredictor;
