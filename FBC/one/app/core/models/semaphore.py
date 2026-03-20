# app/core/models/semaphore.py
from enum import Enum
from typing import Dict, Tuple


class TrafficLightState(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


class TrafficLightSystem:
    def __init__(self):
        self.lights: Dict[Tuple[int, int], dict] = {}
        self.cycle_duration = 30.0  # Duración total del ciclo en segundos

    def add_light(self, position: tuple[int, int], cycle_time: int = None):
        """Añade un nuevo semáforo con tiempo aleatorio inicial"""
        import random

        if cycle_time:
            self.cycle_duration = cycle_time

        self.lights[position] = {
            "state": TrafficLightState.RED,
            "timer": random.uniform(0, self.cycle_duration),
            "cycle_time": self.cycle_duration,
        }

    def update(self, delta_time: float):
        """Actualiza el estado de todos los semáforos"""
        for pos, light in self.lights.items():
            light["timer"] += delta_time

            # Resetear timer si supera el ciclo
            if light["timer"] >= light["cycle_time"]:
                light["timer"] = 0.0

            # Actualizar estado basado en el timer
            if light["timer"] < light["cycle_time"] * 0.45:  # 45% del ciclo
                light["state"] = TrafficLightState.RED
            elif light["timer"] < light["cycle_time"] * 0.50:  # 5% del ciclo
                light["state"] = TrafficLightState.YELLOW
            elif light["timer"] < light["cycle_time"] * 0.95:  # 45% del ciclo
                light["state"] = TrafficLightState.GREEN
            else:  # últimos 5% del ciclo
                light["state"] = TrafficLightState.YELLOW

    def get_state(self, position: tuple[int, int]) -> TrafficLightState:
        """Obtiene el estado actual de un semáforo"""
        if position in self.lights:
            return self.lights[position]["state"]
        return TrafficLightState.RED
