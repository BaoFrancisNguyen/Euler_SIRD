# Euler_SIRD
Installation des librairies:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions_app import method_euler_sird, cost_function (fichier des fonctions)
from scipy.optimize import minimize

Charger les données : On récupère les informations réelles.
le fichier .csv doit être dans la même racine que les fichiers .py

Configurer la simulation : On définit comment et sur combien de temps on va rejouer l'épidémie
Optimiser les paramètres : On teste plusieurs réglages pour trouver ceux qui collent le mieux aux données.
Simuler avec les meilleurs réglages : On recrée l'épidémie avec ces paramètres idéaux.
Comparer : On ajuste les points et on vérifie si la simulation correspond aux données réelles.