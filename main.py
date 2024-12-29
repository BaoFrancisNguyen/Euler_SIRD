import matplotlib.pyplot as plt
from functions_app import method_euler_sird

if __name__ == "__main__":
    # Paramètres épidémiologiques
    beta = 0.3  # Taux de transmission
    gamma = 0.1  # Taux de guérison
    mu = 0.01   # Taux de mortalité

    # Conditions initiales
    S0 = 0.99  # 99% de la population est initialement susceptible
    I0 = 0.01  # 1% de la population est infectée
    R0 = 0.0   # 0% rétabli au départ
    D0 = 0.0   # 0% décédé au départ

    # Paramètres de simulation
    delta_t = 0.01  # Pas de temps (en jours)
    duration = 160  # Durée totale de la simulation (en jours)

    # Appel de la fonction pour simuler le modèle SIRD
    time, S, I, R, D = euler_sird(beta, gamma, mu, S0, I0, R0, D0, delta_t, duration)

    # Visualisation des résultats
    plt.figure(figsize=(10, 6))
    plt.plot(time, S, label="Susceptibles (S)", linewidth=2)
    plt.plot(time, I, label="Infectés (I)", linewidth=2)
    plt.plot(time, R, label="Rétablis (R)", linewidth=2)
    plt.plot(time, D, label="Décédés (D)", linewidth=2)
    plt.xlabel("Temps (jours)", fontsize=12)
    plt.ylabel("Proportion de la population", fontsize=12)
    plt.title("Modèle SIRD - Simulation de la propagation d'une maladie", fontsize=14)
    plt.legend()
    plt.grid()
    plt.show()

