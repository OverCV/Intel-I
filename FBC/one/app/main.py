# app\main.py
import arcade
from visualization.window import SimulationWindow


def main():
    window = SimulationWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
