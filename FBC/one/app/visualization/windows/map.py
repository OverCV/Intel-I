# app/visualization/windows/map.py
from core.models.vehicle import Vehicle
from config.consts import SCREEN_HEIGHT, SCREEN_WIDTH
from visualization.windows.base import BaseWindow


class MapWindow(BaseWindow):
    """Maneja la creación y gestión del mapa"""

    def setup(self):
        self.create_grid_map(10, 10)
        self.add_test_vehicles(3)

    def create_grid_map(self, rows: int, cols: int):
        """Create a grid-based city map."""
        cell_width = SCREEN_WIDTH / (cols + 1)
        cell_height = SCREEN_HEIGHT / (rows + 1)

        # Create intersections dictionary for visualization
        self.intersections = {}

        # First create all intersections
        for row in range(rows):
            for col in range(cols):
                x = (col + 1) * cell_width
                y = (row + 1) * cell_height
                pos = (col, row)
                self.intersections[pos] = (x, y)

                # Add traffic lights at alternating intersections
                if (row + col) % 2 == 0:
                    # Añadir al CityMap (que ahora maneja su propio sistema de semáforos)
                    self.city_map.add_traffic_light(pos, cycle_time=30)

        # Then create all streets (connections between intersections)
        for row in range(rows):
            for col in range(cols):
                current_pos = (col, row)

                # Add horizontal connections
                if col < cols - 1:
                    next_pos = (col + 1, row)
                    self.city_map.add_street(current_pos, next_pos, direction="both")

                # Add vertical connections
                if row < rows - 1:
                    next_pos = (col, row + 1)
                    self.city_map.add_street(current_pos, next_pos, direction="both")

        # Add bus stops along the diagonal
        for i in range(min(rows, cols)):
            pos = (i, i)
            coord = self.intersections[pos]
            self.city_map.add_bus_stop(pos)
            self.bus_stops.append(coord)

    def add_test_vehicles(self, num_vehicles: int):
        """Add test vehicles at random intersections"""
        import random

        intersections = list(self.intersections.values())

        for i in range(num_vehicles):
            # Elegir una intersección aleatoria
            pos = random.choice(intersections)

            # Crear el vehículo
            vehicle = Vehicle(id=f"V{i+1}", position=pos)
            self.vehicle_manager.vehicles[vehicle.id] = vehicle
