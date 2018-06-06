# Dependencias
from sklearn import model_selection, metrics, linear_model
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from scipy import linalg
import random
import tensorflow as tf
import numpy as np
import pandas as pd

# Cargar datos de entrenamiento y prueba y asignarlos a nuestras variables
#Conjunto total de datos
X = pd.read_csv('data.txt', sep=" ", header=None)
y = pd.read_csv('labels.txt', header=None)
X = X.as_matrix()
y = y.as_matrix()

#Conjunto de entrenamiento
X_train = pd.read_csv('data_train.txt', sep=" ", header=None)
y_train = pd.read_csv('labels_train.txt',header=None)
X_train = X_train.as_matrix()
y_train = y_train.as_matrix()

#Conjunto de prueba
X_test = pd.read_csv('data_test.txt', sep=" ", header=None)
y_test = pd.read_csv('labels_test.txt', header=None)
X_test = X_test.as_matrix()
y_test = y_test.as_matrix()

labels_target = ["Maligno","Benigno"]

X_train.shape, y_train.shape, X_test.shape, y_test.shape, X.shape, y.shape

# Visualizar los datos

# Implementacion PCA(Analisis de componentes principales) para poder visualizar los datos 2D
Sigma = (1/X.shape[0]) * np.dot(X.transpose(),X)
U, s, Vh = linalg.svd(Sigma)
Ureduce = U[:,0:2] # Reducimos la dimensiones 30D a 2D
z = np.dot(X,Ureduce)

init_notebook_mode()

scatter = Scatter(
    x = z[:,0],
    y = z[:,1],
    mode = "markers"
)

iplot(dict(
    data = [scatter], 
    layout = dict(
        title = "Benigno(1) vs Maligno(0)",
        xaxis = dict(
            title = "X",
            zeroline = False
        ),
        yaxis = dict(
            title = "y",
            zeroline = False
        )
    )
))