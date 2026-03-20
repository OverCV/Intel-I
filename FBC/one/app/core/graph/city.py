# app/core/graph/city.py
import networkx as nx

from core.models.semaphore import TrafficLightSystem
from core.models.vehicle import Vehicle


class CityMap:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.traffic_system = TrafficLightSystem()
        self.vehicles: dict[str, Vehicle] = {}
        self.bus_stops: list[tuple[float, float]] = []

        # Mapeos para convertir entre nodos y coordenadas
        self.node_to_coord = {}  # Mapea nodos a coordenadas
        self.coord_to_node = {}  # Mapea coordenadas a nodos

        self.passenger_requests = []
        self.points_of_interest = []
        self.active_trips = {}

    def add_street(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        direction: str = "both",
        weight: float = 1.0,
    ):
        """Add a street segment to the city map."""
        # Asegurar que las coordenadas estén en los mapeos
        if start not in self.coord_to_node:
            node_id = len(self.coord_to_node)
            self.coord_to_node[start] = node_id
            self.node_to_coord[node_id] = start

        if end not in self.coord_to_node:
            node_id = len(self.coord_to_node)
            self.coord_to_node[end] = node_id
            self.node_to_coord[node_id] = end

        # Obtener los nodos correspondientes
        start_node = self.coord_to_node[start]
        end_node = self.coord_to_node[end]

        # Añadir la calle al grafo
        if direction in ["both", "forward"]:
            self.graph.add_edge(start_node, end_node, weight=weight)
        if direction in ["both", "backward"]:
            self.graph.add_edge(end_node, start_node, weight=weight)

    def add_traffic_light(self, position: tuple[float, float], cycle_time: int):
        """Add a traffic light at an intersection."""
        self.traffic_system.add_light(position, cycle_time)

        # Asegurar que la posición está en el grafo
        if position not in self.coord_to_node:
            node_id = len(self.coord_to_node)
            self.coord_to_node[position] = node_id
            self.node_to_coord[node_id] = position

    def add_bus_stop(self, position: tuple[float, float]):
        """Add a bus stop at a position."""
        self.bus_stops.append(position)

        # Asegurar que la posición está en el grafo
        if position not in self.coord_to_node:
            node_id = len(self.coord_to_node)
            self.coord_to_node[position] = node_id
            self.node_to_coord[node_id] = position

    def update_traffic_lights(self, delta_time: float):
        """Update all traffic lights in the system."""
        self.traffic_system.update(delta_time)

    def get_traffic_light_state(self, position: tuple[float, float]):
        """Get the state of a traffic light at a position."""
        return self.traffic_system.get_state(position)

    def find_shortest_path(
        self, start: tuple[float, float], end: tuple[float, float], criterion="distance"
    ) -> list[tuple[float, float]]:
        """
        Encuentra la ruta más corta entre dos puntos y retorna la lista de coordenadas
        """
        # Convertir coordenadas a nodos
        if start not in self.coord_to_node or end not in self.coord_to_node:
            return []

        start_node = self.coord_to_node[start]
        end_node = self.coord_to_node[end]

        try:
            # Obtener el camino usando networkx
            path = nx.shortest_path(
                self.graph, source=start_node, target=end_node, weight="weight"
            )

            # Convertir nodos a coordenadas
            return [self.node_to_coord[node] for node in path]
        except nx.NetworkXNoPath:
            return []
