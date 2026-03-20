# app\core\models\vehicle.py
from enum import Enum


class VehicleState(Enum):
    IDLE = "idle"  # Disponible para recoger pasajeros
    PICKING_UP = "pickup"  # En camino a recoger
    PICKED_UP = "picked"  # En camino a recoger
    IN_TRIP = "trip"  # Llevando pasajero al destino


class Vehicle:
    def __init__(self, id: str, position: tuple[float, float]):
        self.id = id
        self.position = position
        self.state = VehicleState.IDLE
        self.route = []
        self.destination = None
        self.speed = 100  # pixels per second
