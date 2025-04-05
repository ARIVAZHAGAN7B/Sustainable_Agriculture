import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)

    encoders = {}
    for col in df.columns:
        if df[col].dtype == 'object':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le

    return df, encoders