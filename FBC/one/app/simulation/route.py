# app/simulation/route.py
import networkx as nx
from core.models.vehicle import Vehicle, VehicleState


class RouteHandler:
    def __init__(self, city_map):
        self.city_map = city_map

    def handle_pickup_selection(self, vehicles, destination_coords, criterion):
        """
        Encuentra el mejor vehículo para recoger al pasajero basado en el criterio
        """
        best_vehicle = None
        best_route = None
        best_score = float("inf")

        # Encontrar el nodo más cercano al destino en el grafo
        destination_node = self._find_closest_node(destination_coords)

        for vehicle in vehicles:
            if vehicle.state != VehicleState.IDLE:
                continue

            # Encontrar el nodo más cercano al vehículo
            start_node = self._find_closest_node(vehicle.position)

            try:
                path = []
                if criterion == "distance":
                    path = nx.shortest_path(
                        self.city_map.graph,
                        source=start_node,
                        target=destination_node,
                        weight="weight",
                    )
                elif criterion == "time":
                    path = self._get_time_optimized_path(start_node, destination_node)
                elif criterion == "fuel":
                    path = self._get_fuel_efficient_path(start_node, destination_node)
                elif criterion == "cost":
                    path = self._get_cost_optimized_path(start_node, destination_node)

                # Convertir los nodos del grafo a coordenadas
                route = [self.city_map.node_to_coord[node] for node in path]

                score = self._calculate_route_score(route, criterion)

                if score < best_score:
                    best_score = score
                    best_vehicle = vehicle
                    best_route = route

            except nx.NetworkXNoPath:
                continue

        if best_vehicle:
            best_vehicle.state = VehicleState.PICKING_UP
            return best_vehicle, best_route
        return None, None

    def handle_destination_selection(
        self, vehicle, destination_coords, criterion, tour_mode=False
    ):
        """
        Calcula la ruta al destino para un vehículo específico
        """
        start_node = self._find_closest_node(vehicle.position)
        destination_node = self._find_closest_node(destination_coords)

        if tour_mode:
            return self._calculate_tour_route(start_node, destination_node)

        try:
            path = []
            if criterion == "distance":
                path = nx.shortest_path(
                    self.city_map.graph,
                    source=start_node,
                    target=destination_node,
                    weight="weight",
                )
            elif criterion == "time":
                path = self._get_time_optimized_path(start_node, destination_node)
            elif criterion == "fuel":
                path = self._get_fuel_efficient_path(start_node, destination_node)
            elif criterion == "cost":
                path = self._get_cost_optimized_path(start_node, destination_node)

            # Convertir los nodos del grafo a coordenadas
            return [self.city_map.node_to_coord[node] for node in path]

        except nx.NetworkXNoPath:
            return None

    def _find_closest_node(self, coords):
        """
        Encuentra el nodo más cercano en el grafo a las coordenadas dadas
        """
        min_distance = float("inf")
        closest_node = None

        for node in self.city_map.graph.nodes():
            node_coords = self.city_map.node_to_coord[node]
            dx = node_coords[0] - coords[0]
            dy = node_coords[1] - coords[1]
            distance = dx * dx + dy * dy

            if distance < min_distance:
                min_distance = distance
                closest_node = node

        return closest_node

    def _calculate_route_score(self, path, criterion):
        """Calcula el score de una ruta según el criterio"""
        total_distance = 0
        for i in range(len(path) - 1):
            dx = path[i + 1][0] - path[i][0]
            dy = path[i + 1][1] - path[i][1]
            total_distance += (dx * dx + dy * dy) ** 0.5

        if criterion == "distance":
            return total_distance
        elif criterion == "time":
            # Contar semáforos en la ruta
            traffic_lights = sum(
                1 for pos in path if pos in self.city_map.traffic_system.lights
            ) 
            return total_distance + traffic_lights * 30
        elif criterion == "fuel":
            # Penalizar cambios de dirección
            direction_changes = 0
            for i in range(len(path) - 2):
                if self._is_turn(path[i], path[i + 1], path[i + 2]):
                    direction_changes += 1
            return total_distance + direction_changes * 20
        elif criterion == "cost":
            return total_distance * 1.5  # Precio base por distancia
        return total_distance

    def _is_turn(self, p1, p2, p3):
        """Determina si hay un giro entre tres puntos"""
        dx1 = p2[0] - p1[0]
        dy1 = p2[1] - p1[1]
        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]
        return abs(dx1) != abs(dx2) or abs(dy1) != abs(dy2)
