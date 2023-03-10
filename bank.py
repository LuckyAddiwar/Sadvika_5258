# -*- coding: utf-8 -*-
"""Untitled.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TqiX1rs4lJMSvQa5r0cN2OwyuKhyphTV
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

dataset = pd.read_csv('BankNote_Authentication.csv')

X = dataset.iloc[:, :4]
y = dataset.iloc[:, -1]

regressor = LogisticRegression()

regressor.fit(X, y)

