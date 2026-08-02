import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "maternal_risk_model.pkl"
ENCODER_PATH = BASE_DIR / "models" / "label_encoder.pkl"

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)


def predict_risk(
    age,
    systolic_bp,
    diastolic_bp,
    blood_sugar,
    body_temp,
    heart_rate
):

    patient = pd.DataFrame({
        "Age": [age],
        "SystolicBP": [systolic_bp],
        "DiastolicBP": [diastolic_bp],
        "BS": [blood_sugar],
        "BodyTemp": [body_temp],
        "HeartRate": [heart_rate]
    })

    prediction = model.predict(patient)

    probabilities = model.predict_proba(patient)[0]

    risk = label_encoder.inverse_transform(prediction)[0]

    confidence = probabilities.max()

    probability_dict = {
        label: float(prob)
        for label, prob in zip(label_encoder.classes_, probabilities)
    }

    return risk, confidence, probability_dict