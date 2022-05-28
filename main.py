import pandas as pd
import numpy as np


def readData(path):
    data = pd.read_csv(path)
    return data


def __main__():
    path = "german_credit_data.csv  "
    df = readData(path)

    # Check Datafield
    print("Datafield\n", df.head, "\n")
    print("Jumlah data dan fitur\n", df.shape, "\n")
    print("Jenis Data\n", df.dtypes, "\n")
    print(df.info)
    df.replace("?", np.nan, inplace=True)
    print(df.isnull().sum())
    print(df.isnull().any())
    print(df.dropna())


__main__()
