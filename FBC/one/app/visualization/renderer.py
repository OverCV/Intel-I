# app/visualization/renderer.py
import arcade
from core.models.vehicle import Vehicle, VehicleState
from core.models.semaphore import TrafficLightState, TrafficLightSystem


class Renderer:
    def draw_all(
        self,
        intersections: dict[tuple[float, float]],
        traffic_system: TrafficLightSystem,
        vehicles: dict[str, Vehicle],
        selected_vehicle: Vehicle,
        bus_stops: list[tuple[float, float]],
    ):
        """Dibuja todos los elementos de la simulación"""
        # 1. Dibujar calles
        self._draw_roads(intersections)

        # 2. Dibujar semáforos
        for pos in intersections:
            if pos in traffic_system.lights:
                state = traffic_system.get_state(pos)
                self._draw_traffic_light(intersections[pos], state)

        # 3. Dibujar paradas de bus
        for stop in bus_stops:
            self._draw_bus_stop(stop)

        # 4. Dibujar vehículos y rutas
        for vehicle in vehicles.values():
            # Dibujar ruta si existe
            if vehicle.route:
                color = (
                    arcade.color.GREEN
                    if vehicle == selected_vehicle
                    else arcade.color.GRAY
                )
                self._draw_route(vehicle.route, color)

            # Dibujar vehículo
            self._draw_vehicle(vehicle, vehicle == selected_vehicle)

    def _draw_roads(self, intersections):
        """Dibuja la red de calles"""
        for pos1 in intersections:
            x1, y1 = intersections[pos1]
            for pos2 in intersections:
                x2, y2 = intersections[pos2]
                # Dibujar solo si son adyacentes
                if (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or (
                    pos1[0] == pos2[0] and abs(pos1[1] - pos2[1]) == 1
                ):
                    arcade.draw_line(x1, y1, x2, y2, arcade.color.GRAY, 2)

    def _draw_traffic_light(self, position, state):
        """Dibuja un semáforo individual"""
        color = {
            TrafficLightState.RED: arcade.color.RED,
            TrafficLightState.GREEN: arcade.color.GREEN,
            TrafficLightState.YELLOW: arcade.color.YELLOW,
        }[state]

        x, y = position
        arcade.draw_circle_filled(x, y, 5, color)

    def _draw_bus_stop(self, position):
        """Dibuja una parada de bus"""
        x, y = position
        arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE)

    def _draw_vehicle(self, vehicle: Vehicle, is_selected):
        """Dibuja un vehículo"""
        x, y = vehicle.position

        # Color según estado
        color = arcade.color.YELLOW  # Default
        if is_selected:
            color = arcade.color.GREEN
        elif vehicle.state == VehicleState.IDLE:
            color = arcade.color.YELLOW

        arcade.draw_circle_filled(x, y, 8, color)
        arcade.draw_text(vehicle.id, x - 10, y + 10, arcade.color.BLACK, 8)

    def _draw_route(self, route, color):
        """Dibuja una ruta"""
        if len(route) < 2:
            return

        for i in range(len(route) - 1):
            x1, y1 = route[i]
            x2, y2 = route[i + 1]
            arcade.draw_line(x1, y1, x2, y2, color, 2)
