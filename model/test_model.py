import pandas as pd
import joblib

print("Loading model...")

model = joblib.load(
    "model/fraud_model.pkl"
)


print("Loading data...")

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


sample = df[
    features
].head(20)


predictions = model.predict(
    sample
)


result = sample.copy()

result["prediction"] = predictions


print(result)
