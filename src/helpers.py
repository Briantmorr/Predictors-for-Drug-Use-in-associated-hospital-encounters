import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  

def multivariant_analysis(df, hue, type):
    int_vars = df.select_dtypes(include = ['int','float'])
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(15,15))
    axs = axs.flatten()

    for i, var in enumerate (int_vars):
        if var != 'time':
            if type == 'kde':
                sns.kdeplot(x=var,data=df,hue=hue,ax=axs[i])
            elif type == 'hist':
                sns.histplot(x=var,data=df,hue=hue,ax=axs[i])
            elif type == 'box':
                sns.boxplot(x=var,data=df, y=hue,ax=axs[i])
            axs[i].set_title(var)

    plt.tight_layout()
    plt.show()

def load_csv(url: str) -> pd.DataFrame:
    return pd.read_csv(url)