import logging
from pathlib import Path

from http_client_lab.client import HttpClient


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    client = HttpClient(timeout=5.0, max_retries=3)

    url = "https://httpbin.org/image/png"
    output = Path("downloads") / "image.png"

    try:
        client.download_file(url, output)
    except Exception as e:
        logging.critical(f"Error fatal: {e}")


if __name__ == "__main__":
    main()