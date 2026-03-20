# app/core/managers/vehicle.py
from typing import Optional
import math
from core.models.vehicle import Vehicle, VehicleState


class VehicleManager:
    def __init__(self):
        self.vehicles: dict[str, Vehicle] = {}

    def add_vehicle(self, position: tuple[float, float]) -> str:
        vehicle_id = f"V{len(self.vehicles) + 1}"
        self.vehicles[vehicle_id] = Vehicle(id=vehicle_id, position=position)
        return vehicle_id

    def get_available_vehicles(self):
        """Retorna solo los vehículos en estado IDLE"""
        return [v for v in self.vehicles.values() if v.state == VehicleState.IDLE]

    def find_nearest_vehicle(
        self, position: tuple[float, float], criterion: str = "distance"
    ) -> Optional[Vehicle]:
        """
        Encuentra el vehículo más adecuado según el criterio especificado
        Solo considera vehículos en estado IDLE
        """
        best_score = float("inf")
        best_vehicle = None

        for vehicle in self.get_available_vehicles():
            dx = vehicle.position[0] - position[0]
            dy = vehicle.position[1] - position[1]
            distance = math.sqrt(dx * dx + dy * dy)

            # Calcular score según el criterio
            score = {
                "distance": distance,
                "time": distance * 1.2
                if abs(dx) > abs(dy)
                else distance,  # Penalizar rutas con más giros
                "fuel": distance
                * (1.0 + abs(dy) / (abs(dx) + 1e-6)),  # Penalizar subidas
                "cost": distance * vehicle.cost_per_km,
            }.get(criterion, distance)

            if score < best_score:
                best_score = score
                best_vehicle = vehicle

        return best_vehicle

    def update_vehicle_position(
        self, vehicle: Vehicle, delta_time: float, simulation_speed: float
    ):
        """Actualiza la posición del vehículo en su ruta"""
        if not vehicle.route:
            return

        next_point = vehicle.route[0]
        dx = next_point[0] - vehicle.position[0]
        dy = next_point[1] - vehicle.position[1]
        distance = math.sqrt(dx * dx + dy * dy)

        # Si llegamos al siguiente punto
        if distance < 2.0:  # Tolerancia para considerar llegada
            vehicle.position = next_point
            vehicle.route.pop(0)

            # Si la ruta está vacía, actualizar estado
            if not vehicle.route:
                if vehicle.state == VehicleState.PICKING_UP:
                    vehicle.state = VehicleState.PICKED_UP
                elif vehicle.state == VehicleState.IN_TRIP:
                    vehicle.state = VehicleState.IDLE
                    vehicle.destination = None
        else:
            # Mover hacia el siguiente punto
            # Calculamos la velocidad considerando el delta time y la velocidad de simulación
            speed = vehicle.speed * delta_time * simulation_speed

            # Normalizamos el movimiento para mantener la velocidad constante
            ratio = speed / distance

            # Actualizamos la posición
            new_x = vehicle.position[0] + dx * ratio
            new_y = vehicle.position[1] + dy * ratio
            vehicle.position = (new_x, new_y)

    def get_vehicle_by_id(self, vehicle_id: str) -> Optional[Vehicle]:
        """Obtiene un vehículo por su ID"""
        return self.vehicles.get(vehicle_id)

    def reset_vehicle(self, vehicle: Vehicle):
        """Resetea el estado de un vehículo"""
        vehicle.state = VehicleState.IDLE
        vehicle.route = []
        vehicle.destination = None
