"""Etapa 2 del laboratorio.

TODO estudiante:
1. Leer data/processed/clientes.csv.
2. Entrenar una LogisticRegression.
3. Guardar models/model.pkl.
4. Guardar metrics.json con accuracy.
"""
from pathlib import Path

DATA = Path("data/processed/clientes.csv")
MODEL = Path("models/model.pkl")
METRICS = Path("metrics.json")


def main() -> None:
    raise NotImplementedError("Completar la etapa de entrenamiento")


if __name__ == "__main__":
    main()
