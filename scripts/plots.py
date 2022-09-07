import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(df: pd.DataFrame, column: str, group:str) -> None:
    plt.figure(figsize=(20, 10))
    fig = sns.countplot(data=df, x=column,
                        order=df[column].value_counts().index)
    plt.title(f'Distribution of {column} in {group} set', size=20, fontweight='bold')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(column, fontsize=20)
    plt.ylabel('Absolute frequencies', fontsize=20)
    for i in range(len(df[column].value_counts())):
        fig.text(i, (df[column].value_counts().values[i]), str('{:.1f}%'.format(100 * df[column].value_counts().values[i] / len(df[column]))),
                 fontdict=dict(color='black', fontsize=30), horizontalalignment='center')


def tsHueplot(x, y, hue, title:str):
    plt.figure(figsize=(24,10))
    plt.title(title)
    sns.lineplot(x, y, hue=hue)

def factorplot(df: pd.DataFrame, x, y, col, hue, row):
    sns.factorplot(data = df, x = x, y = y, col = col, palette = 'plasma', hue = hue, row = row)
    
def autocorrelation(df: pd.DataFrame, column: str, title: str):
    plt.rc("figure", figsize=(10,6))
    plt.title(title)
    pd.plotting.autocorrelation_plot(df[column])

def countplot(df: pd.DataFrame, x: str, hue: str, order: list, title: str, ncolors: int):
    plt.figure(figsize=(20,10))
    sns.countplot(x=x, hue=hue, order=order, data=df,
        palette=sns.color_palette("Set2", n_colors=ncolors)).set_title(title)

def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col, hue=hue, style=style)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)

