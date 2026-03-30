import pandas as pd


def load_and_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # eliminar filas con nulos
    df = df.dropna()

    return df