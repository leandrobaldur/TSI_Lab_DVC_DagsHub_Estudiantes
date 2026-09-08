"""Etapa 1 del laboratorio.

TODO estudiante:
1. Leer data/raw/clientes.csv.
2. Eliminar duplicados y filas con nulos.
3. Crear ingresos_miles = ingresos / 1000.
4. Guardar data/processed/clientes.csv.
"""
from pathlib import Path

RAW = Path("data/raw/clientes.csv")
OUTPUT = Path("data/processed/clientes.csv")


def main() -> None:
    raise NotImplementedError("Completar la etapa de preparacion")


if __name__ == "__main__":
    main()
