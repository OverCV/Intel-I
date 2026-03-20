import gym
from gym.spaces import Discrete


class Scenario:
    """Class Frozen_lake is used to maange the gym envrionment."""

    def __init__(self, FROZEN_LAKE_ENV="FrozenLake-v0") -> None:
        self.env = gym.make(FROZEN_LAKE_ENV)

        self.states: Discrete = self.env.observation_space
        self.actions: Discrete = self.env.action_space
        self.transition: dict[
            int,
            dict[
                int,
                list[
                    tuple[float, int, float, bool],
                    tuple[float, int, float, bool],
                    tuple[float, int, float, bool],
                ],
            ],
        ] = self.env.P

        # self.num_states: int = self.states.n
        # self.num_actions: int = self.actions.n

    def get_env(self):
        return self.env


scene = Scenario()
