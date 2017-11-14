import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import configparser

if __name__ == '__main__':
    inifile = configparser.SafeConfigParser()
    inifile.read('./config.ini')
    df = pd.read_csv(
        inifile.get('perceptron', 'iris_dataset_url'), header=None)
    print(df.tail())
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = df.iloc[0:100, [0, 2]].values
    plt.scatter(
        X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
    plt.scatter(
        X[50:100, 0],
        X[50:100, 1],
        color='blue',
        marker='x',
        label='versicolor')
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()
