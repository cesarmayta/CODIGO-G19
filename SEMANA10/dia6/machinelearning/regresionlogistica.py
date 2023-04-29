import pandas as pd
import sklearn
from scipy.sparse import random

import matplotlib.pyplot as plt

#para PCA
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

#para preparar nuestra data
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split



if __name__ == "__main__":
    df_heart = pd.read_csv('./datasets/heart.csv')
    print(df_heart.head(5))
    
    df_features = df_heart.drop(['target'],axis=1)
    df_target = df_heart['target']
    
    #normalizando nuestro dataframe
    df_features = StandardScaler().fit_transform(df_features)
    
    #ENTRENAMIENTO DEL MODELO
    x_train,x_test,y_train,y_test = train_test_split(df_features,df_target,
                                                     test_size=0.3,
                                                     random_state=42)
    
    print(x_train.shape)
    print(y_train.shape)
    
    #APLICAMOS PCA
    pca = PCA(n_components=3)
    pca.fit(x_train)
    
    #aplicando modelos de regresión logistica
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    
    logistic = LogisticRegression(solver='lbfgs')
    #configurar datos de entrenamiento
    df_train = pca.transform(x_train)
    df_test = pca.transform(x_test)
    #entrenamos el modelo
    logistic.fit(df_train,y_train)
    print('Score/Accuracy PCA:',logistic.score(df_test,y_test))
    
    #predicción
    x_new = np.array([54,1,0])
    prediccion = logistic.predict(x_new.reshape(1,-1))
    print("una persona con 54 años sexo masculino :")
    if(prediccion == 1):
        print("puede sufrir ataca al corazón")
    else:
        print("no sufriria ataque el corazón")
    