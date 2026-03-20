# app\core\models\user_trip.py
from dataclasses import dataclass


@dataclass
class PassengerRequest:
    pickup: tuple[float, float]  # Punto de recogida
    dropoff: tuple[float, float]  # Destino
    time: float  # Tiempo de solicitud
    route_preference: str  # "shortest", "fastest", "fuel", "economic"
    is_tour: bool = False  # Si es servicio Tour-Trip


@dataclass
class Trip:
    vehicle_id: str
    request: PassengerRequest
    start_time: float
    route: list[tuple[float, float]]
    status: str  # "picking_up", "in_progress", "completed"
