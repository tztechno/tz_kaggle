import matplotlib.pyplot as plt
import seaborn as sns

def kde_hue(df, grouped_column):
    fig = sns.FacetGrid(df, hue=grouped_column, aspect=4)
    fig.map(sns.kdeplot, 'num_sold', shade=True)
    max_value = df['num_sold'].max()
    fig.set(xlim=(0,max_value))
    fig.add_legend()
    
    grouped = df.groupby(grouped_column).mean()
