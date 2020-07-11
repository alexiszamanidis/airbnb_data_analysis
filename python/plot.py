import seaborn as sns
import matplotlib.pyplot as plt

"""
plot_bar: plots a bar pattern depending on the input
                        
arguments:
    dataframe: pandas dataframe
    x:         string
    y:         string
    title:     string
    xlabel:    string
    xlabel:    string
    color:     string
"""
def plot_bar(dataframe, x, y, title, xlabel, ylabel, color):
    dataframe.plot(kind = "bar", 
                   x = x,
                   y = y,
                   color = color,
                   figsize = (20,10), 
                   title = title,
                   legend = False)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

"""
plot_map: plots a map pattern depending on the input
                        
arguments:
    dataframe:        pandas dataframe
    longitude_column: string
    latitude_column:  string
    column:           string
"""
def plot_map(dataframe, longitude_column, latitude_column, column):
    plt.figure(figsize=(10,6))
    sns.scatterplot(dataframe[longitude_column], dataframe[latitude_column], hue = dataframe[column])
    plt.ioff()

"""
plot_heat_map: plots a heat map pattern depending on the input
                        
arguments:
    dataframe:     pandas dataframe
    group_by_list: [string]
    column:        string
    mode:          string
    cmap:          string
    title:         string
    xlabel:        string
    xlabel:        string
"""
def plot_heat_map(dataframe, group_by_list, column, mode, cmap, title, xlabel, ylabel):
    plt.figure(figsize=(15,15))
    if mode == "count":
        sns.heatmap(dataframe.groupby(group_by_list)[column].count().unstack(),annot=True, fmt=".0f", cmap=cmap)
    elif mode == "mean":
        sns.heatmap(dataframe.groupby(group_by_list)[column].mean().unstack(),annot=True, fmt=".0f", cmap=cmap)
    plt.title(title, fontsize = 20)
    plt.xlabel(xlabel,fontsize = 15)
    plt.ylabel(ylabel,fontsize = 15)
    plt.show()