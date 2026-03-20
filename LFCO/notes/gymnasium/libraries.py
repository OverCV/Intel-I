import gym
import numpy as np
from scenario import scene

# Constantes
GAMMA = 0.99
THETA = 1e-10

ARROWS: list[str] = ['←', '↓', '→', '↑']
ACTIONS: dict = { i: arrow for i, arrow in enumerate(ARROWS) }