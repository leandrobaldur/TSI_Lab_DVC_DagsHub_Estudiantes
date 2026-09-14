from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

DATA = Path("data/processed/clientes.csv")
MODEL = Path("models/model.pkl")
METRICS = Path("metrics.json")

def main() -> None:
    df = pd.read_csv(DATA)

    features = ["edad", "ingresos_miles", "visitas"]
    X = df[features]
    y = df["compro"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    MODEL.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL)
    METRICS.write_text(
        json.dumps({"accuracy": accuracy}, indent=2), encoding="utf-8"
    )

    print(f"Accuracy: {accuracy:.3f}")

if __name__ == "__main__":
    main()