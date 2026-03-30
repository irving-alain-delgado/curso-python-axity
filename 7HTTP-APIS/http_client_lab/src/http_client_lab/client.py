import logging
import time
from pathlib import Path

import httpx


class HttpClient:
    def __init__(self, timeout: float = 5.0, max_retries: int = 3) -> None:
        self.timeout = timeout
        self.max_retries = max_retries

    def download_file(self, url: str, output_path: Path) -> None:
        attempts = 0

        while attempts < self.max_retries:
            try:
                logging.info(f"Intento {attempts + 1} de descarga")

                with httpx.stream(
                    "GET",
                    url,
                    timeout=self.timeout,
                ) as response:
                    response.raise_for_status()

                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    with output_path.open("wb") as file:
                        for chunk in response.iter_bytes():
                            file.write(chunk)

                logging.info("Descarga completada correctamente")
                return

            except httpx.TimeoutException:
                logging.warning("Timeout ocurrido")

            except httpx.HTTPStatusError as e:
                logging.error(f"Error HTTP: {e.response.status_code}")
                raise

            except httpx.RequestError as e:
                logging.warning(f"Error de red: {e}")

            attempts += 1
            time.sleep(2 * attempts)

        raise RuntimeError("No se pudo completar la descarga tras varios intentos")