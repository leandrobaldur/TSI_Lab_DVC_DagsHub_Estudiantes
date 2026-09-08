from pathlib import Path


def test_raw_dataset_exists() -> None:
    assert Path("data/raw/clientes.csv").exists()


def test_pipeline_definition_exists() -> None:
    assert Path("dvc.yaml").exists()
