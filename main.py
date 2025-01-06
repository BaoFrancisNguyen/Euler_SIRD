import matplotlib.pyplot as plt
import pandas as pd
from functions_app import method_euler_sird, cost_function



# Charger les données empiriques
data = pd.read_csv('sird_dataset.csv')

# Extraire les données
time_data = data['time'].values
S_data = data['S'].values
I_data = data['I'].values
R_data = data['R'].values
D_data = data['D'].values

# Convertir les données en dictionnaire
data_dict = {'S': S_data, 'I': I_data, 'R': R_data, 'D': D_data}

# Paramètres initiaux
S0, I0, R0, D0 = S_data[0], I_data[0], R_data[0], D_data[0] # Conditions initiales
delta_t = 0.01 # Pas
duration = time_data[-1] # Durée totale de la simulation

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

# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.plot(time, S, label="Susceptibles (S)", linewidth=2)
plt.plot(time, I, label="Infectés (I)", linewidth=2)
plt.plot(time, R, label="Rétablis (R)", linewidth=2)
plt.plot(time, D, label="Décédés (D)", linewidth=2)
plt.xlabel("Temps (jours)", fontsize=12)
plt.ylabel("Proportion de la population", fontsize=12)
plt.title("Modèle SIRD - Simulation de la propagation d'une maladie", fontsize=10)
plt.legend()
plt.grid()
plt.show()


# test de la fonction method_euler_sird sur une journée:
# légère diminution des susceptibles, augmentation des infectés


