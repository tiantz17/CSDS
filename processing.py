# preprocessing the raw data

import numpy as np
import pandas as pd

def readfile(filename):
    df = pd.read_excel(filename, skiprows=1)
    df = df.dropna(axis=1,thresh=7)
    for j in df.columns:
        print(j)
        for i in df.index:
            #print(df[j][i])
            #print(df[j][i].replace('\n', ''))
            try:
                df.loc[i, j] = df[j][i].replace('\n', '')
            except:
                pass
            #print(df[j][i])
    df.to_csv(filename[:-4] + '-0.csv', sep='\t', encoding='utf-8', index=False)
    df = pd.read_csv(filename[:-4] + '-0.csv', sep='\t')
    return df
