import random
from pythonic_utils.decorators import retry
from pythonic_utils.generators import batch_generator
from pythonic_utils.context_managers import timer


@retry(max_attempts=3, delay=1)
def unstable_task():
    if random.random() < 0.7:
        raise ValueError("Fallo aleatorio")
    return "✅ Éxito"


def main():
    print("Probando retry...\n")
    try:
        print(unstable_task())
    except Exception as e:
        print(f"Falló definitivamente: {e}")

    print("\nProbando generador por lotes...\n")

    data = list(range(10))

    for batch in batch_generator(data, 3):
        print(batch)

    print("\nProbando context manager timer...\n")

    with timer():
        sum(range(10_000_000))


if __name__ == "__main__":
    main()