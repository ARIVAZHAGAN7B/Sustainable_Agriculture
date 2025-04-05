import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("market_researcher_dataset.csv")
df.dropna(inplace=True)

# Encode categorical columns
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    joblib.dump(le, f"market_label_encoder.pkl")

# Define features & target
features = [
    'Product',
    'Demand_Index',
    'Supply_Index',
    'Competitor_Price_per_ton',
    'Economic_Indicator',
    'Weather_Impact_Score',
    'Seasonal_Factor',
    'Consumer_Trend_Index'
]
target = 'Market_Price_per_ton'

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMarket Price Model Performance:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Cross-validated MAE: {-cv_scores.mean():.2f}")
print(f"R² Score: {r2:.2f}")

# Save model
joblib.dump(model, "market_price_model.pkl")
print("✅ Model saved as market_price_model.pkl")

# Feature Importance Plot
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': importances}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df, hue='Feature', legend=False, palette='crest')
plt.title("Feature Importance for Market Price Prediction")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
