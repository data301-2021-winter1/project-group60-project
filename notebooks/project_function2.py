import pandas as pd
import numpy as np
def unprocess(csv_file):
    df=pd.read_csv(csv_file)
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df_clean=df.copy().drop(['region'],axis=1)
    df_clean1=df_clean.copy().drop(['children'],axis=1)
    df_sorted=df_clean1.sort_values("age")
    return df_sorted
#def Age(dfp):
#         df1=dfp.groupby('age',as_index=False).sum()
#         return df1
def Age(dfp):
    df = dfp.groupby('age', as_index=False).sum()
    return df

def bmia(dfp):
    df20 = dfp.groupby('bmi', as_index=False).sum()
    return df20
def sort_age(dfp):
    df1=dfp.groupby("age",as_index=False).sum()
    for i in range (18,64):
        df2=pd.melt(df1,id_vars='age',value_vars=[i])
        return df2
def sort_genre(dfp):
    df1 = dfp.groupby("age", as_index=False).sum()
    df2 = pd.melt(df1, id_vars="bmi", value_vars=["charges"])
    return df2
   