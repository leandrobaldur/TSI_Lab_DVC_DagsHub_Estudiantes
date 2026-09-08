# TSI - Starter del Laboratorio DVC + DagsHub + Data Lineage

Este repositorio inicial esta preparado para seguir la **Guia del Estudiante** desde Visual Studio Code en Windows.

## Flujo recomendado

1. Lea `INICIO_RAPIDO.md`.
2. Abra la carpeta en VS Code.
3. Ejecute `uv sync`.
4. Verifique `uv run pytest` y `uv run ruff check .`.
5. Inicie Git y DVC durante el laboratorio.
6. Siga la guia Word incluida.

## Meta del laboratorio

Completar y ejecutar el pipeline:

```text
data/raw/clientes.csv
        |
        v
     preparar
        |
        v
data/processed/clientes.csv
        |
        v
     entrenar
      /     \
     v       v
model.pkl  metrics.json
```

Los archivos `src/preparar.py` y `src/entrenar.py` se entregan incompletos de manera intencional.

> Seguridad: nunca versionar tokens, contrasenas ni `.dvc/config.local`.
