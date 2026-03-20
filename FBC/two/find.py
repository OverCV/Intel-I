# find.py
import numpy as np
from queue import PriorityQueue
from dataclasses import dataclass


@dataclass
class Node: 
    id: int
    position: tuple[float, float]
    is_intersection: bool = False
    has_traffic_light: bool = False


class CityGraph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.adj_matrix = np.zeros((num_nodes, num_nodes), dtype=float)
        self.nodes: dict[int, Node] = {}

    def add_node(
        self,
        node_id: int,
        position: tuple[float, float],
        is_intersection: bool = False,
        has_traffic_light: bool = False,
    ):
        """Add a node to the graph."""
        self.nodes[node_id] = Node(
            node_id, position, is_intersection, has_traffic_light
        )

    def add_edge(self, from_node: int, to_node: int, weight: float = 1.0):
        """Add a directed edge to the graph."""
        self.adj_matrix[from_node][to_node] = weight

    def add_bidirectional_edge(self, node1: int, node2: int, weight: float = 1.0):
        """Add a bidirectional edge between two nodes."""
        self.add_edge(node1, node2, weight)
        self.add_edge(node2, node1, weight)

    def get_neighbors(self, node: int) -> list[tuple[int, float]]:
        """Get all neighbors of a node with their weights."""
        neighbors = []
        for i in range(self.num_nodes):
            if self.adj_matrix[node][i] > 0:
                neighbors.append((i, self.adj_matrix[node][i]))
        return neighbors

    def dijkstra(self, start: int, end: int) -> tuple[list[int], float]:
        """Find the shortest path between two nodes using Dijkstra's algorithm."""
        distances = np.full(self.num_nodes, np.inf)
        distances[start] = 0
        previous = np.full(self.num_nodes, -1)

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            current_distance, current = pq.get()

            if current == end:
                break

            if current_distance > distances[current]:
                continue

            for neighbor, weight in self.get_neighbors(current):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    pq.put((distance, neighbor))

        # Reconstruct path
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path, distances[end]

    def a_star(self, start: int, end: int) -> tuple[list[int], float]:
        """Find the shortest path using A* algorithm."""

        def heuristic(node1: int, node2: int) -> float:
            """Calculate Euclidean distance between two nodes."""
            x1, y1 = self.nodes[node1].position
            x2, y2 = self.nodes[node2].position
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        distances = np.full(self.num_nodes, np.inf)
        distances[start] = 0
        previous = np.full(self.num_nodes, -1)

        pq = PriorityQueue()
        pq.put((0 + heuristic(start, end), start))

        while not pq.empty():
            _, current = pq.get()

            if current == end:
                break

            for neighbor, weight in self.get_neighbors(current):
                distance = distances[current] + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    priority = distance + heuristic(neighbor, end)
                    pq.put((priority, neighbor))

        # Reconstruct path
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path, distances[end]

    def bellman_ford(self, start: int) -> tuple[np.ndarray, np.ndarray]:
        """Find shortest paths from start to all nodes using Bellman-Ford algorithm."""
        distances = np.full(self.num_nodes, np.inf)
        distances[start] = 0
        previous = np.full(self.num_nodes, -1)

        # Relax edges repeatedly
        for _ in range(self.num_nodes - 1):
            for u in range(self.num_nodes):
                for v, weight in self.get_neighbors(u):
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        previous[v] = u

        # Check for negative cycles
        for u in range(self.num_nodes):
            for v, weight in self.get_neighbors(u):
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains negative cycles")

        return distances, previous


class CityMapBuilder:
    """Helper class to construct city maps."""

    @staticmethod
    def create_grid(rows: int, cols: int, bidirectional: bool = True) -> CityGraph:
        """Create a grid-based city map."""
        num_nodes = rows * cols
        graph = CityGraph(num_nodes)

        # Add nodes
        for row in range(rows):
            for col in range(cols):
                node_id = row * cols + col
                position = (col * 100, row * 100)  # Scale positions for visualization
                is_intersection = True
                has_traffic_light = (row + col) % 2 == 0  # Alternating traffic lights
                graph.add_node(node_id, position, is_intersection, has_traffic_light)

        # Add edges
        for row in range(rows):
            for col in range(cols):
                current = row * cols + col

                # Add horizontal edges
                if col < cols - 1:
                    if bidirectional:
                        graph.add_bidirectional_edge(current, current + 1)
                    else:
                        graph.add_edge(current, current + 1)

                # Add vertical edges
                if row < rows - 1:
                    if bidirectional:
                        graph.add_bidirectional_edge(current, current + cols)
                    else:
                        graph.add_edge(current, current + cols)

        return graph
