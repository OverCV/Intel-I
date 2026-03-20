# app\visualization\window.py
from visualization.windows.input import InputWindow
from visualization.windows.map import MapWindow
from visualization.windows.render import RenderWindow


class SimulationWindow(MapWindow, InputWindow, RenderWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    # Este es el que realmente se está usando
    def update(self, delta_time: float):
        super().update(delta_time)  # Llama al update de BaseWindow
