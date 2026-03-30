import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from ds_lab.preprocess import load_and_clean


def train_model():
    df = load_and_clean("data/sample.csv")

    X = df[["age", "income"]]
    y = df["bought"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    print("Modelo entrenado y guardado.")


if __name__ == "__main__":
    train_model()