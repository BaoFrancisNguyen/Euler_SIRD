import matplotlib.pyplot as plt
from functions_app import method_euler_sird

#paramètres donnés
beta = 0.5
gamma = 0.15
mu = 0.015
S0 = 0.99
I0 = 0.01
R0 = 0.0
D0 = 0.0
delta_t = 0.01
duration = 100  #simulation pour 100 jours

#simulation avec la méthode d'Euler
time, S, I, R, D = method_euler_sird(beta, gamma, mu, S0, I0, R0, D0, delta_t, duration)

#courbes
plt.figure(figsize=(12, 8))
plt.plot(time, S, label="Susceptibles (S)", color='blue')
plt.plot(time, I, label="Infectés (I)", color='red')
plt.plot(time, R, label="Rétablis (R)", color='green')
plt.plot(time, D, label="Décès (D)", color='black')

plt.title("Simulation SIRD", fontsize=16)
plt.xlabel("Temps (jours)", fontsize=12)
plt.ylabel("Proportion de la population", fontsize=12)
plt.legend(fontsize=10)
plt.grid()
plt.show()