# fonction de calcul de la solution approchée du modèle SIRD par la méthode d'Euler explicite
# paramètres entrées : beta, gamma, mu, S0, I0, R0, D0, delta_t, duration
# beta : taux de transmission
# gamma : taux de guérison
# mu : taux de mortalité
# S0 : population saine initiale
# I0 : population infectée initiale
# R0 : population guérie initiale
# D0 : population décédée initiale
# delta_t : pas de temps
# duration : durée de la simulation
# paramètres sortie : S, I, R, D
# S : population saine
# I : population infectée
# R : population guérie
# D : population décédée

import numpy as np
import matplotlib.pyplot as plt

def euler_sird(beta, gamma, mu, S0, I0, R0, D0, delta_t, duration):
