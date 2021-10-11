# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:57:11 2021

@author: tonat
"""
import string
import pandas as pd
import numpy as np
import scipy.spatial.distance as sc

class CDIN:
    ## Metodos para exploración de datos
    
    def dqr(x):
        cols = pd.DataFrame(list(x.columns.values),
                            columns=['Name'],
                            index=list(x.columns.values))
        dtyp = pd.DataFrame(x.dtypes, columns=['Type'])
        misval = pd.DataFrame(x.isnull().sum(),
                              columns=['N/A value'])
        presval = pd.DataFrame(x.count(),
                               columns=['Count values'])
        unival = pd.DataFrame(columns=['Unique values'])
        minval = pd.DataFrame(columns=['Min'])
        maxval = pd.DataFrame(columns=['Max'])
        mean = pd.DataFrame(x.mean(), columns=['Mean'])
        Std = pd.DataFrame(x.std(), columns=['Std'])
        Var = pd.DataFrame(x.var(), columns=['Var'])
        median = pd.DataFrame(x.median(), columns=['Median'])
        percentage_mis = pd.DataFrame(x.isnull().sum() / x.shape[0] * 100, columns = ['% Data Missing'])
        percentage_present = pd.DataFrame(x.count()/ x.shape[0] * 100, columns = ['% Data Present'])
    
        #skewness = pd.DataFrame(x.skew(), columns=['Skewness'])
        #kurtosis = pd.DataFrame(x.kurtosis(), columns=['Kurtosis'])
    
        for col in list(x.columns.values):
            unival.loc[col] = [x[col].nunique()]
            try:
                minval.loc[col] = [x[col].min()]
                maxval.loc[col] = [x[col].max()]
            except:
                pass

    # Juntar todas las tablas
        return cols.join(dtyp).join(misval).join(presval).join(unival).join(minval).join(maxval).join(mean).join(Std).join(
        Var).join(median).join(percentage_mis).join(percentage_present) #.join(skewness).join(kurtosis)
    
    
    
    ## Metodos para limpieza de datos
    
    # Funcion para remover signos de puntuación

    def remover_punctuation(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except:
            pass
        return x
    
    # Función para remover digitos

    def remove_digits(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.digits)
        except:
            pass
        return x
    
    # Función para remover espacios en blancos
    
    def remove_whitespace(x):
        try:
            x = ''.join(x.split())
        except:
            pass
        return x
    
    # Función para remplazar texto

    def replace_text(x, to_replace, replacement):
        try:
            x = x.replace(to_replace, replacement)
        except:
            pass
        return x
    
    # Función para convertir a mayúsculas
    
    def upper_case(x):
        try:
            x = x.upper()
        except:
            pass
        return x
    
    # Función para convertir en minúsculas
    def lower_case(x):
        try:
            x = x.lower()
        except:
            pass
        return x
    
    # Función para remover los espacios en blanco
    
    def white_space(x):
        try:
            x = ''.join(x.splt())
        except:
            pass
        
    # Quita espacios en blanco a la izquierda y derecha
    
    def remove_whitespacelr(x):
        try:
            x = x.lstrip().rstrip()
        except:
            pass
        
    
    # Función para convertir un tipo de variable en Dumi
    
    def get_dummies_nom(df, cat_nominales):
        df_nom_dummy = pd.get_dummies(df[cat_nominales[0]], prefix = cat_nominales[0])
        
        for col in cat_nominales[1:]:
            temp = pd.get_dummies(df[col], prefix = col)
            df_nom_dummy = df_nom_dummy.join(temp)
            
        del temp
        
        return df_nom_dummy
    
    # Funcion que calcula la distancia de similitud
    
    def pdistance(df, metric):
        dist = sc.pdist(df, metric)
        #Matriz de distancias de similitud
        DIST = pd.DataFrame(sc.squareform(dist))
        
        return DIST
    
    
    # Funcion para distancia coseno
    
    def cosine_distance(A,B):
        dot = np.dot(A,B)
        norm_a = np.sqrt(np.dot(A,A))
        norm_b = np.sqrt(np.dot(B,B))
        
        cos = dot/(norm_a * norm_b)
        
        return 1 - cos
        
        
        













    
    