import pandas as pd
import numpy as np

def notprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df1=(df.dropna(subset=["Year_of_Release","Publisher","Critic_Score","Critic_Count","User_Score","User_Count","Developer","Rating"]) 
        .sort_values("Genre")
        .reset_index(drop=True)
        )    
    return df1
    
def year_of_release(dfp):
    df1 = dfp.groupby('Year_of_Release', as_index=False).sum()
    return df1
    
def sort_genre(dfp):
    df1 = dfp.groupby("Genre", as_index=False).sum()
    df2 = pd.melt(df1, id_vars="Genre", value_vars=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"],var_name ='Region', value_name ='Sales')
    return df2

def melt_year_of_release(dfp):
    df1 = dfp.groupby('Year_of_Release', as_index=False).sum()
    df2 = pd.melt(df1, id_vars="Year_of_Release", value_vars=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"],var_name ='Region', value_name ='Sales')
    return df2
    
def genre_mean(dfp):
    return dfp.groupby('Genre', as_index=False).mean()