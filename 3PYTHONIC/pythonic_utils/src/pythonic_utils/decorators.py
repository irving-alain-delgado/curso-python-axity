import time
from functools import wraps


def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Intento {attempts} fallido: {e}")

                    if attempts >= max_attempts:
                        raise

                    time.sleep(delay * attempts)

        return wrapper
    return decorator