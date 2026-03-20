# app/core/managers/traffic.py
from typing import Dict, Tuple
from core.models.semaphore import TrafficLightState


class TrafficLightManager:
    def __init__(self):
        self.lights: Dict[Tuple[int, int], Dict] = {}
        self.cycle_time = 30.0  # Tiempo total del ciclo en segundos

    def add_traffic_light(self, pos: Tuple[int, int]):
        """Añade un nuevo semáforo"""
        self.lights[pos] = {
            "state": TrafficLightState.RED,
            "timer": 0.0,
            "cycle_time": self.cycle_time,
        }

    def update(self, delta_time: float):
        """Actualiza el estado de todos los semáforos"""
        for pos, light in self.lights.items():
            light["timer"] += delta_time

            # Si el timer supera el tiempo del ciclo, reiniciamos
            if light["timer"] >= light["cycle_time"]:
                light["timer"] = 0.0

            # Actualizamos el estado basado en el timer
            if light["timer"] < light["cycle_time"] * 0.45:  # 45% del ciclo
                light["state"] = TrafficLightState.RED
            elif light["timer"] < light["cycle_time"] * 0.50:  # 5% del ciclo
                light["state"] = TrafficLightState.YELLOW
            elif light["timer"] < light["cycle_time"] * 0.95:  # 45% del ciclo
                light["state"] = TrafficLightState.GREEN
            else:  # últimos 5% del ciclo
                light["state"] = TrafficLightState.YELLOW

    def get_state(self, pos: Tuple[int, int]) -> TrafficLightState:
        """Obtiene el estado actual de un semáforo"""
        return (
            self.lights[pos]["state"] if pos in self.lights else TrafficLightState.RED
        )
