import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df=pd.read_csv(csv_file)
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df_clean = df.round(1)
    df_sorted=df_clean.sort_values("age")
    return df_sorted

def replace_object(csv_file):
    df = pd.read_csv(csv_file)
    df.smoker.replace(('yes', 'no'), (1, 0), inplace=True)
    df.sex.replace(('female', 'male'), (1, 0), inplace=True)
    df_clean = df.copy().drop(['region','children'],axis=1)
    df_clean = df_clean.round(1)
    # df.rename(columns = {"smoker": "smoking status",}, inplace = True)
    return df_clean

def byregion(csv_file):
    df = pd.read_csv(csv_file)
    import matplotlib.pylab as plt
    import seaborn as sns
    axk= plt.figure(figsize=(6,6))
    sns.lmplot(x='age', y= 'charges',data=df,markers='.',hue ='region',height=10,aspect=1)
    return plt.title('Responsiveness of the medical bill to age by region')

def bysmoker(csv_file):
    df = pd.read_csv(csv_file)
    import matplotlib.pylab as plt
    import seaborn as sns
    axk= plt.figure(figsize=(6,6))
    sns.lmplot(x='age', y= 'charges',data=df,markers='.',hue ='smoker',height=10,aspect=1)
    return plt.title('Responsiveness of the medical bill to age by smoking status')

def Age(dfp):
    df = dfp.groupby('age', as_index=False).sum()
    return df
                    