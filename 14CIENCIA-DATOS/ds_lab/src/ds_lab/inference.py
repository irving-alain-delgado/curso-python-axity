import joblib
import pandas as pd


def predict(age: int, income: int):
    model = joblib.load("models/model.pkl")

    data = pd.DataFrame([[age, income]], columns=["age", "income"])

    prediction = model.predict(data)

    return prediction[0]


if __name__ == "__main__":
    result = predict(30, 40000)
    print("Predicción:", result)