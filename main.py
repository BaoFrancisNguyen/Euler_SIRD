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

# paramètres début
S0, I0, R0, D0 = S_data[0], I_data[0], R_data[0], D_data[0] # conditions initiales
delta_t = 0.01 # Pas
duration = time_data[-1] # durée totale de la simulation
steps = len(time_data)  #correspondre au nombre de points empiriques

'''if __name__ == "__main__":
    # Paramètres épidémiologiques
    beta = 0.5  # Taux de transmission
    gamma = 0.15  # Taux de guérison
    mu = 0.015   # Taux de mortalité

    # Conditions initiales
    S0 = 0.99  # 99% de la population est initialement susceptible
    I0 = 0.01  # 1% de la population est infectée
    R0 = 0.0   # 0% rétabli au départ
    D0 = 0.0   # 0% décédé au départ

    # Paramètres de simulation
    delta_t = 0.01  # Pas de temps (en jours)
    duration = 1  # Durée totale de la simulation (en jours)

    # Appel de la fonction pour simuler le modèle SIRD
    time, S, I, R, D = method_euler_sird(beta, gamma, mu, S0, I0, R0, D0, delta_t, duration)'''

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

beta_range = np.linspace(0.25, 0.5, 6)
gamma_range = np.linspace(0.08, 0.15, 8)
mu_range = np.linspace(0.005, 0.015, 11)

#optimisation des paramètres
best_params, min_cost = optimize_parameters(beta_range, gamma_range, mu_range)
print(f"Meilleurs paramètres trouvés : β={best_params[0]}, γ={best_params[1]}, μ={best_params[2]} avec un coût de {min_cost}")

#simulation avec les meilleurs paramètres
time_opt, S_opt, I_opt, R_opt, D_opt = method_euler_sird(
    best_params[0], best_params[1], best_params[2], S0, I0, R0, D0, delta_t, duration)

# Visualisation des résultats
plt.figure(figsize=(12, 8))
plt.plot(time_data, I_data, label="Infectés - Empirique", linestyle="--", linewidth=2)
plt.plot(time_opt, I_opt, label="Infectés - Modèle ajusté", linewidth=2)
plt.xlabel("Temps (jours)", fontsize=12)
plt.ylabel("Proportion de la population", fontsize=12)
plt.title("Ajustement du modèle SIRD aux données empiriques", fontsize=14)
plt.legend()
plt.grid()
plt.show()


# test de la fonction method_euler_sird sur une journée:
# légère diminution des susceptibles, augmentation des infectés


