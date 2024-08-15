#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    df = df.drop(columns=['label', 'id', 'attack_cat'])
    
    df = df.fillna(df.median())
    
    features = df[['src_bytes', 'dst_bytes', 'duration', 'sport', 'dport', 'proto']]
    
    # Categorical to numerical
    features = pd.get_dummies(features, columns=['proto'])
    
    # Scaling features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    return scaled_features

if __name__ == "__main__":
    preprocess_data('../data/UNSW_NB15_training-set.csv')

