import csv
import json
import logging
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone


def process_csv(input_path: Path, output_path: Path) -> None:
    logging.info("Iniciando procesamiento de CSV")

    if not input_path.exists():
        logging.error("El archivo no existe")
        raise FileNotFoundError(f"No existe {input_path}")

    totals = defaultdict(float)
    count = 0

    with input_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["amount"])
                category = row["category"]
            except (KeyError, ValueError) as e:
                logging.warning(f"Fila inválida: {row} - {e}")
                continue

            totals[category] += amount
            count += 1

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_records": count,
        "totals_by_category": dict(totals),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)

    logging.info("Procesamiento finalizado correctamente")