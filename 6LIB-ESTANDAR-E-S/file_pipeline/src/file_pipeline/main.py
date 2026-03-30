import logging
from pathlib import Path
from file_pipeline.processor import process_csv


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    input_file = Path("data") / "sales.csv"
    output_file = Path("output") / "report.json"

    try:
        process_csv(input_file, output_file)
    except Exception as e:
        logging.critical(f"Error fatal: {e}")


if __name__ == "__main__":
    main()