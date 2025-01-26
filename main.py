import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions_app import method_euler_sird, cost_function
from scipy.optimize import minimize # pour minimiser la fonction coût avec la méthode de Newton ou de BFGS (Broyden-Fletcher-Goldfarb-Shanno)


#charger les données empiriques à partir du fichier csv
data = pd.read_csv('sird_dataset.csv')

#extraction des données
time_data = data['Jour'].values
S_data = data['Susceptibles'].values
I_data = data['Infectés'].values
R_data = data['Rétablis'].values
D_data = data['Décès'].values

# convertion des données en dictionnaire
data_dict = {'Susceptibles': S_data, 'Infectés': I_data, 'Rétablis': R_data, 'Décès': D_data}

##But:recréer l'histoire de l'épidémie en la rejouant avec les paramètres du modèle SIRD

# configuration de la simulation / paramètres début
S0, I0, R0, D0 = S_data[0], I_data[0], R_data[0], D_data[0] # conditions initiales (état de la population au jour 0)
delta_t = 0.01 # Pas
duration = time_data[-1] # durée totale de la simulation en fonction des données empiriques
steps = len(time_data)  #correspondre au nombre de points empiriques



#On cherche les meilleurs paramètres (β, γ, μ) pour que le modèle colle au mieux aux données empiriques.
#Le modèle simule l'épidémie pour chaque combinaison possible des paramètres.
#Une mesure de l'erreur (cost_function) compare la simulation aux données réelles.
#On garde les paramètres qui donnent la plus petite erreur.

#fonction pour ajuster les paramètres du modèle

def optimize_parameters(beta_range, gamma_range, mu_range):
    best_params = None
    min_cost = float('inf')

    for beta in beta_range:
        for gamma in gamma_range:
            for mu in mu_range:
                time_sim, S_sim, I_sim, R_sim, D_sim = method_euler_sird(
                    beta, gamma, mu, S0, I0, R0, D0, delta_t, duration
                )
                #Si le modèle et les données réelles n'ont pas le même nombre de points dans le temps,
                # on "redimensionne" les résultats du modèle pour qu'ils correspondent aux données:
                # Ajuster les dimensions pour correspondre aux données empiriques
                if len(time_sim) != len(time_data):
                    I_sim_resampled = np.interp(time_data, time_sim, I_sim)
                else:
                    I_sim_resampled = I_sim

                cost = cost_function(I_data, I_sim_resampled)
                if cost < min_cost:
                    min_cost = cost
                    best_params = (beta, gamma, mu)

    return best_params, min_cost

#définition des plages de valeurs pour les paramètres

beta_range = np.linspace(0.25, 0.5, 6) # la plage de valeurs pour beta 0.25 à 0.5 avec 6 valeurs signifie qu'une personne infectée transmet le virus à une autre personne entre 25% et 50% des contacts
gamma_range = np.linspace(0.08, 0.15, 8) # la plage de valeurs pour gamma 0.08 à 0.15 avec 8 valeurs correspond à un délai de guérison de 7 à 12,5 jours
mu_range = np.linspace(0.005, 0.015, 11)#correspond à une mortalité journalière entre 0,5 % et 1,5 % des infectés

#optimisation des paramètres
best_params, min_cost = optimize_parameters(beta_range, gamma_range, mu_range)
print(f"Meilleurs paramètres trouvés : β={best_params[0]}, γ={best_params[1]}, μ={best_params[2]} avec un coût de {min_cost}")


# Une fois les meilleurs paramètres trouvés, on les utilise pour générer une simulation finale
#simulation avec les meilleurs paramètres
time_opt, S_opt, I_opt, R_opt, D_opt = method_euler_sird(
    best_params[0], best_params[1], best_params[2], S0, I0, R0, D0, delta_t, duration)

# Visualisation des résultats
#On trace deux courbes :
#La courbe empirique montre les données réelles
#La courbe simulée montre le modèle ajusté aux données

plt.figure(figsize=(12, 8))
plt.plot(time_data, I_data, label="Infectés - Empirique", linestyle="--", linewidth=2)
plt.plot(time_opt, I_opt, label="Infectés - Modèle ajusté", linewidth=2)
plt.xlabel("Temps (jours)", fontsize=12)
plt.ylabel("Proportion de la population", fontsize=12)
plt.title("Ajustement du modèle SIRD aux données empiriques", fontsize=14)
plt.legend()
plt.grid()
plt.show()



