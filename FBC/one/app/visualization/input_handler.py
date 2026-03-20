# app/visualization/input_handler.py
import arcade
import math

from core.models.vehicle import Vehicle, VehicleState
from config.consts import SCREEN_WIDTH, SCREEN_HEIGHT


class InputHandler:
    def find_nearest_intersection(
        self, window, x: float, y: float
    ) -> tuple[float, float]:
        """Encuentra la intersección más cercana al click"""
        min_distance = float("inf")
        nearest_pos = None

        for pos in window.intersections.values():
            dx = pos[0] - x
            dy = pos[1] - y
            distance = math.sqrt(dx * dx + dy * dy)

            if distance < min_distance:
                min_distance = distance
                nearest_pos = pos

        return nearest_pos

    def handle_key_press(self, window, key, modifiers):
        """Maneja los inputs de teclado"""
        if key == arcade.key.SPACE:
            window.paused = not window.paused
        elif key == arcade.key.UP:
            window.simulation_speed = min(4.0, window.simulation_speed * 1.5)
        elif key == arcade.key.DOWN:
            window.simulation_speed = max(0.25, window.simulation_speed / 1.5)

    def handle_control_panel_click(self, window, x: float, y: float) -> bool:
        """Maneja clicks en el panel de control"""
        if x < SCREEN_WIDTH:  # Si el click no está en el panel, ignorar
            return False

        # Coordenadas iniciales del panel
        start_x = SCREEN_WIDTH + 20
        current_y = SCREEN_HEIGHT - 40

        # Verificar click en criterios de optimización
        criteria_start_y = current_y - 100
        criteria = ["distance", "time", "fuel", "cost"]
        button_height = 30

        for i, criterion in enumerate(criteria):
            check_y = criteria_start_y - (button_height * i)
            if (
                start_x <= x <= start_x + 150
                and check_y - button_height <= y <= check_y
            ):
                window.state_manager.current_criterion = criterion
                return True

        return False

    def handle_pickup_click(self, window, clicked_pos):
        """Maneja click en fase de recogida"""
        # Encontrar el vehículo más cercano según el criterio actual
        vehicles: list[Vehicle] = window.vehicle_manager.vehicles.values()
        nearest_vehicle = None
        min_distance = float("inf")

        for vehicle in vehicles:
            if vehicle.state == VehicleState.IDLE:
                dx = vehicle.position[0] - clicked_pos[0]
                dy = vehicle.position[1] - clicked_pos[1]
                distance = math.sqrt(dx * dx + dy * dy)

                if distance < min_distance:
                    min_distance = distance
                    nearest_vehicle = vehicle

        if nearest_vehicle:
            # TODO: Obtener ruta usando window.city_map
            route = [nearest_vehicle.position, clicked_pos]  # Temporal, directo
            return nearest_vehicle, route

        return None, None

    def handle_destination_click(self, window, clicked_pos):
        """Maneja click en fase de destino"""
        vehicle: Vehicle = window.state_manager.selected_vehicle
        if vehicle:
            # TODO: Obtener ruta usando window.city_map
            route = [vehicle.position, clicked_pos]  # Temporal, directo
            return route
        return None
