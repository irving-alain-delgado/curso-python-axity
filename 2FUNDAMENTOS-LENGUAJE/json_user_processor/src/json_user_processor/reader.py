import json
from pathlib import Path


def read_json(path: str) -> list[dict]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("El JSON debe contener una lista de objetos.")

            return data

    except json.JSONDecodeError as e:
        raise ValueError("El archivo no contiene JSON válido.") from e