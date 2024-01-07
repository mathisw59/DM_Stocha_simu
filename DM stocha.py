# Author: Mathis WAUQUIEZ
# Date: 2024-01-07
# Python version: 3.7
# Objectif : Simuler l'évolution de la population d'une espèce


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

n_generations = 100

Z = 50

Ms = []

dist = [0.2, .6, .2] # distribution du nombre d'enfants
choices = np.arange(len(dist))

# distribution du nombre d'enfants selon la loi de Poisson
# mean = 1
# dist = np.exp(-mean) * mean**choices / np.math.factorial(choices)

mean = sum(choices*dist)

fig, ax = plt.subplots()
ax.set_xlim(0, n_generations)
ax.set_ylim(0, Z * 2)
ax.set_xlabel('Generation')
ax.set_ylabel('Y')

# On met un titre au graphique
ax.set_title(r'Evolution de la population pour $Z_0 = {}$ et $\mu = {:.4f}$'.format(Z, mean))

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return (line,)

def animate(i):
    global Z, Ms
    X = np.random.choice(choices, Z, p=dist)
    Z = sum(X)
    assert Z < 100000, "Z = {} is too big, interrupting simulation".format(Z)
    
    M = Z / mean**i

    Ms.append(M)

    # get the ylim
    ylim = ax.get_ylim()
    if M > ylim[1]:
        ax.set_ylim(ylim[0], mas(Ms)*2)
    
    x = np.arange(len(Ms))
    y = Ms

    if i == 0:
        ax.set_ylim(0, max(y) * 2)
        Ms = []
        Z = 50
    
    line.set_data(x, y)
    return (line,)

anim_duration = 10 # seconds
interval = anim_duration * 1000 / n_generations # milliseconds

anim = animation.FuncAnimation(fig, animate, init_func=init,
                                 frames=n_generations, interval=interval, blit=True)

plt.show()