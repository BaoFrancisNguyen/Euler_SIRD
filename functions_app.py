# fonction de calcul de la solution approchée du modèle SIRD par la méthode d'Euler explicite


# paramètres entrées: beta, gamma, mu, S0, I0, R0, D0, delta_t, duration
# beta: taux de transmission
# gamma: taux de guérison
# mu: taux de mortalité
# S0: population saine initiale
# I0: population infectée initiale
# R0: population guérie initiale
# D0: population décédée initiale
# delta_t: pas de temps
# duration: durée de la simulation

# paramètres sortie : S, I, R, D
# S: population saine
# I: population infectée
# R: population guérie
# D: population décédée

# on va créer des tableaux pour stocker les valeurs de S, I, R, D à chaque pas de temps >>> en utilisant np.zeros()
# on va initialiser les valeurs de S, I, R, D à t=0 >>> en utilisant les valeurs initiales S0, I0, R0, D0
# on va calculer les valeurs de S, I, R, D à chaque pas de temps en utilisant la méthode d'Euler explicite >>> en utilisant une boucle for

# on va retourner les valeurs de S, I, R, D


# importation des bibliothèques

import numpy as np
import matplotlib.pyplot as plt

#initialisation des paramètres

beta = 0.3 #taux de transmission
gamma = 0.1 #taux de guérison
mu = 0.05 #taux de mortalité
S0 = 0.99 #population saine initiale
I0 = 0.01 #population infectée initiale
R0 = 0 #population guérie initiale
D0 = 0 #population décédée initiale
delta_t = 0.01 #pas de temps
duration = 100 #durée de la simulation

#initialisation des variables
steps = int(duration / delta_t)


def euler_sird(beta, gamma, mu, S0, I0, R0, D0, delta_t, duration):

