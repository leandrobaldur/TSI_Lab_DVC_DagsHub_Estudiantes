from pathlib import Path
import pandas as pd

RAW = Path("data/raw/clientes.csv")
OUTPUT = Path("data/processed/clientes.csv")

def main() -> None:
    df = pd.read_csv(RAW)
    df = df.drop_duplicates()
    df = df.dropna()
    df["ingresos_miles"] = df["ingresos"] / 1000

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print(f"Dataset procesado: {len(df)} registros")

if __name__ == "__main__":
    main()