# logic.py
import networkx as nx
from dataclasses import dataclass
from typing import Optional
from enum import Enum


class TrafficLightState(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


@dataclass
class TrafficLight:
    id: str
    position: tuple[float, float]
    cycle_time: int  # Total time for a complete cycle
    state: TrafficLightState = TrafficLightState.RED
    time_in_state: float = 0


class VehicleState(Enum):
    IDLE = "idle"  # Esperando solicitud
    PICKING_UP = "picking"  # Yendo a recoger pasajero
    IN_TRIP = "in_trip"  # Llevando pasajero a destino


@dataclass
class Vehicle:
    id: str
    position: tuple[float, float]
    state: VehicleState = VehicleState.IDLE
    route: list[tuple[float, float]] = None
    destination: Optional[tuple[float, float]] = None
    speed: float = 100.0  # pixels per second


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


class CityMap:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.traffic_lights: dict[str, TrafficLight] = {}
        self.vehicles: dict[str, Vehicle] = {}
        self.bus_stops: list[tuple[float, float]] = []

        self.passenger_requests = []  # Lista de solicitudes pendientes
        self.points_of_interest = []  # Puntos turísticos para Tour-Trip
        self.active_trips = {}  # Viajes en curso

    def add_street(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        direction: str = "both",
        weight: float = 1.0,
    ):
        """Add a street segment to the city map."""
        if direction in ["both", "forward"]:
            self.graph.add_edge(start, end, weight=weight)
        if direction in ["both", "backward"]:
            self.graph.add_edge(end, start, weight=weight)

    def add_traffic_light(self, position: tuple[float, float], cycle_time: int):
        """Add a traffic light at an intersection."""
        light_id = f"light_{len(self.traffic_lights)}"
        self.traffic_lights[light_id] = TrafficLight(
            id=light_id, position=position, cycle_time=cycle_time
        )

    def add_vehicle(self, position: tuple[float, float], fuel_efficiency: float = 10.0):
        """Add a vehicle to the system."""
        vehicle_id = f"vehicle_{len(self.vehicles)}"
        self.vehicles[vehicle_id] = Vehicle(
            id=vehicle_id, position=position, fuel_efficiency=fuel_efficiency
        )
        return vehicle_id

    def add_bus_stop(self, position: tuple[float, float]):
        """Add a bus stop to the system."""
        self.bus_stops.append(position)

    def find_shortest_path(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        criterion: str = "distance",
    ) -> list[tuple[float, float]]:
        """
        Find the optimal path based on different criteria:
        - distance: shortest path
        - time: fastest path considering traffic lights
        - fuel: most fuel-efficient path
        - cost: most economical path for passengers
        """
        if criterion == "distance":
            return nx.shortest_path(self.graph, start, end, weight="weight")
        elif criterion == "time":
            # Consider traffic lights in weight calculation
            return self._find_time_optimal_path(start, end)
        elif criterion == "fuel":
            # Consider elevation and traffic for fuel consumption
            return self._find_fuel_optimal_path(start, end)
        elif criterion == "cost":
            # Consider distance and fixed costs
            return self._find_cost_optimal_path(start, end)

        raise ValueError(f"Unknown criterion: {criterion}")

    def update_traffic_lights(self, dt: float):
        """Update the state of all traffic lights."""
        for light in self.traffic_lights.values():
            light.time_in_state += dt
            if light.time_in_state >= light.cycle_time:
                light.time_in_state = 0
                if light.state == TrafficLightState.RED:
                    light.state = TrafficLightState.GREEN
                elif light.state == TrafficLightState.GREEN:
                    light.state = TrafficLightState.YELLOW
                else:
                    light.state = TrafficLightState.RED

    def update_vehicles(self, dt: float):
        """Update the position of all vehicles based on their routes."""
        for vehicle in self.vehicles.values():
            if vehicle.route:
                # Simple movement along route
                # In a real implementation, consider traffic lights and other vehicles
                next_point = vehicle.route[0]
                # Update position (simplified)
                vehicle.position = next_point
                vehicle.route.pop(0)

    def generate_trip_report(self, vehicle_id: str) -> dict:
        """Generate a detailed report for a completed trip."""
        vehicle = self.vehicles[vehicle_id]
        # This would be populated with actual trip data in a real implementation
        return {
            "cost": 0.0,
            "streets_traversed": 0,
            "duration": 0.0,
            "fuel_consumption": 0.0,
            "route_comparison": {},
        }

    def _find_time_optimal_path(self, start, end):
        """Find the fastest path considering traffic lights."""
        # Implementation would consider traffic light timing
        return nx.shortest_path(self.graph, start, end)

    def _find_fuel_optimal_path(self, start, end):
        """Find the most fuel-efficient path."""
        # Implementation would consider elevation and vehicle characteristics
        return nx.shortest_path(self.graph, start, end)

    def _find_cost_optimal_path(self, start, end):
        """Find the most economical path for passengers."""
        # Implementation would consider distance and fare structure
        return nx.shortest_path(self.graph, start, end)
