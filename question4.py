
 #R0>1 :

##Chaque personne infectée, en moyenne, contamine plus d'une personne.

#R0<1 :

##Chaque personne infectée, en moyenne, contamine moins d'une
#  personne.

##On va comparer deux simulations :

##Sans intervention (
#𝛽 = 0.5

#Avec intervention (
#β réduit à 0.3


import matplotlib.pyplot as plt
from functions_app import method_euler_sird

# Paramètres pour les deux scénarios
params_no_intervention = {
    'beta': 0.5,
    'gamma': 0.15,
    'mu': 0.015,
    'S0': 0.99,
    'I0': 0.01,
    'R0': 0.0,
    'D0': 0.0,
    'delta_t': 0.01,
    'duration': 100
}

params_with_intervention = params_no_intervention.copy()
params_with_intervention['beta'] = 0.3  #réduction du taux de transmission

#simulation sans intervention
time_no, S_no, I_no, R_no, D_no = method_euler_sird(**params_no_intervention)

#simulation avec intervention
time_with, S_with, I_with, R_with, D_with = method_euler_sird(**params_with_intervention)

#tracé des courbes pour comparaison
plt.figure(figsize=(14, 8))

#Sans intervention
plt.plot(time_no, I_no, label="Infectés (sans intervention)", linestyle="--", color='red')
plt.plot(time_no, R_no, label="Rétablis (sans intervention)", linestyle="--", color='green')
plt.plot(time_no, D_no, label="Décès (sans intervention)", linestyle="--", color='black')

#Avec intervention
plt.plot(time_with, I_with, label="Infectés (avec intervention)", color='red')
plt.plot(time_with, R_with, label="Rétablis (avec intervention)", color='green')
plt.plot(time_with, D_with, label="Décès (avec intervention)", color='black')

#configuration du graphique
plt.title("Comparaison des scénarios : avec et sans intervention", fontsize=16)
plt.xlabel("Temps (jours)", fontsize=12)
plt.ylabel("Proportion de la population", fontsize=12)
plt.legend(fontsize=10)
plt.grid()
plt.show()

#Observations:
#Dans le scénario sans intervention, le nombre d'infectés
#augmente rapidement, entraînant une augmentation du nombre de 
#décès
#Dans le scénario avec intervention, il y a réduction du taux de
# transmission