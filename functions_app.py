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

# on va créer des tableaux pour stocker les valeurs de S, I, R, D à chaque pas >>> en utilisant np.zeros() >>> S[0], S[1], ..., S[100]...
# on va initialiser les valeurs de S, I, R, D à t=0 >>> en utilisant les valeurs initiales S0, I0, R0, D0
# on va calculer les valeurs de S, I, R, D à chaque pas de temps en utilisant la méthode d'Euler explicite >>> en utilisant une boucle for

# on va retourner:
    #time (numpy.ndarray): Tableau des temps simulés.
    # S, I, R, D (numpy.ndarray): Tableaux des proportions de la population.


# importation des bibliothèques
import numpy as np

def euler_sird(beta, gamma, mu, S0, I0, R0, D0, delta_t, duration):

    # Calcul du nombre total de pas de temps
    steps = int(duration / delta_t)

    # Création des tableaux pour enregistrer les résultats
    S = np.zeros(steps)
    I = np.zeros(steps)
    R = np.zeros(steps)
    D = np.zeros(steps)
    time = np.linspace(0, duration, steps)

    # Initialisation des conditions initiales
    S[0] = S0
    I[0] = I0
    R[0] = R0
    D[0] = D0

    # Simulation de l'évolution à l'aide de la méthode d'Euler
    for temps in range(steps - 1):
        S[temps + 1] = S[temps] + delta_t * (-beta * S[temps] * I[temps])
        I[temps + 1] = I[temps] + delta_t * (beta * S[temps] * I[temps] - gamma * I[temps] - mu * I[temps])
        R[temps + 1] = R[temps] + delta_t * (gamma * I[temps])
        D[temps + 1] = D[temps] + delta_t * (mu * I[temps])

    return time, S, I, R, D
