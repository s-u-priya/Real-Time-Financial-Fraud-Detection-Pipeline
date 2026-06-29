import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest


print("Loading dataset...")

df = pd.read_csv(
    "data/paysim.csv"
)


features = [

    "amount",

    "oldbalanceOrg",

    "newbalanceOrig",

    "oldbalanceDest",

    "newbalanceDest"

]


X = df[features]


print("Training model...")


model = IsolationForest(

    contamination=0.01,

    random_state=42

)


model.fit(X)


joblib.dump(
    model,
    "model/fraud_model.pkl"
)


print("Model saved")