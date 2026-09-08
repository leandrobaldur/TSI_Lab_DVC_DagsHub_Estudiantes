# Inicio rapido - Laboratorio DVC + DagsHub + Data Lineage

## 1. Descomprimir y abrir en VS Code

1. Descomprima el ZIP en una carpeta de trabajo, por ejemplo `C:\TSI\Lab_DVC_DagsHub`.
2. Abra **Visual Studio Code**.
3. Seleccione **File > Open Folder...** y abra la carpeta descomprimida.
4. Si VS Code muestra recomendaciones de extensiones, instale las sugeridas.

## 2. Abrir la terminal integrada

En VS Code seleccione **Terminal > New Terminal**. La guia usa PowerShell.

Compruebe:

```powershell
git --version
uv --version
python --version
```

Si `uv` no esta instalado, instalelo antes de continuar segun las instrucciones de la guia.

## 3. Crear el entorno del proyecto

```powershell
uv sync
```

Esto crea `.venv` e instala las dependencias declaradas en `pyproject.toml`.

Compruebe:

```powershell
uv run python --version
uv run dvc version
uv run pytest
uv run ruff check .
```

Los tests iniciales solo verifican que el starter tenga los archivos base esperados.

## 4. Iniciar Git y DVC

Este starter se entrega intencionalmente sin `.git/` ni `.dvc/`, para que usted realice esos pasos durante el laboratorio.

```powershell
git init
uv run dvc init
```

Luego continue con la guia Word incluida en esta carpeta.

## 5. Regla importante sobre credenciales

No escriba tokens ni contrasenas de DagsHub en archivos versionados. Cuando la guia configure el remoto DVC, use `--local` para las credenciales. DVC las guardara en `.dvc/config.local`, que esta excluido de Git.

## 6. Archivos principales

- `pyproject.toml`: define el entorno Python y sus dependencias.
- `dvc.yaml`: describe el pipeline y sus relaciones de dependencia.
- `src/preparar.py`: etapa de preparacion que debe completar.
- `src/entrenar.py`: etapa de entrenamiento que debe completar.
- `data/raw/clientes.csv`: dataset inicial del laboratorio.
- `tests/`: comprobaciones del starter.

## 7. Si VS Code no detecta Python

Presione `Ctrl+Shift+P`, ejecute **Python: Select Interpreter** y seleccione:

```text
.venv\Scripts\python.exe
```

No use un interprete global si `.venv` ya fue creado por `uv sync`.
