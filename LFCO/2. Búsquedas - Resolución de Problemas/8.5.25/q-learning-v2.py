from gymnasium import Env, spaces
import numpy as np


class Laberinto(Env):
    def __init__(self):
        super().__init__()

        self.laberinto = np.array(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ]
        )

        self.pos_inicial = (0, 0)
        self.pos_final = (4, 4)

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple((spaces.Discrete(5), spaces.Discrete(5)))
    