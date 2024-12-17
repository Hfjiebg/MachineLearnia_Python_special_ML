traduction = {
 'chien': 'dog',
 'chat': 'cat',
 'souris': 'mouse',
 'oiseau' : 'bird'
 }


inventaire = {
 'bananes': 5000,
 'pommes': 2094,
 'poires': 412809
 }

dictionnaire_3 = {
    'dict_1' : traduction,
    'dict_2' : inventaire
    }

import numpy as np

parametres = {
    'W1': np.random.randn(10, 100),
    'b1': np.random.randn(10, 1),
    'W2': np.random.randn(10, 10),
    'b2': np.random.randn(10, 1), 
    }