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
    
    plt.plot(pca.explained_variance_)
    plt.show()