# app/visualization/windows/base.py
import arcade

from core.models.vehicle import VehicleState
from core.graph.city import CityMap
from core.managers.vehicle import VehicleManager
from core.managers.traffic import TrafficLightManager
from simulation.route import RouteHandler
from simulation.state import SimulationStateManager
from visualization.input_handler import InputHandler
from visualization.renderer import Renderer

from debug.panel import DebugPanel

from config.consts import (
    CONTROL_PANEL_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SCREEN_TITLE,
)


class BaseWindow(arcade.Window):
    """Clase base que maneja la inicialización básica de la ventana"""

    def __init__(self):
        super().__init__(
            SCREEN_WIDTH + CONTROL_PANEL_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
        )
        arcade.set_background_color(arcade.color.WHITE)
        self.debug_panel = DebugPanel()

        # Managers y handlers
        self.city_map = CityMap()
        self.vehicle_manager = VehicleManager()
        self.traffic_manager = TrafficLightManager()
        self.input_handler = InputHandler()
        self.renderer = Renderer()
        self.state_manager = SimulationStateManager()
        self.route_handler = RouteHandler(self.city_map)

        # Control de simulación
        self.paused = False
        self.simulation_speed = 1.0

        # Estructuras de datos del mapa
        self.intersections = {}
        self.bus_stops = []

    def update(self, delta_time: float):
        if not self.paused:
            # Actualizar semáforos usando el sistema del CityMap
            self.city_map.update_traffic_lights(delta_time * self.simulation_speed)

            # Actualizar vehículos
            for vehicle in self.vehicle_manager.vehicles.values():
                # Log estado inicial
                self.debug_panel.log(f"Vehicle {vehicle.id}: {vehicle.state}")

                # Solo actualizar si tiene una ruta
                if vehicle.route:
                    self.vehicle_manager.update_vehicle_position(
                        vehicle, delta_time, self.simulation_speed
                    )

                    # Si el vehículo completó su ruta
                    if not vehicle.route:
                        if vehicle.state == VehicleState.PICKING_UP:
                            # Si estaba recogiendo, cambiar a fase de destino
                            self.state_manager.switch_to_destination_phase(vehicle)
                        elif vehicle.state == VehicleState.IN_TRIP:
                            # Si terminó el viaje, volver a estado IDLE
                            vehicle.state = VehicleState.IDLE
                            if vehicle == self.state_manager.selected_vehicle:
                                self.state_manager.reset_to_pickup_phase()

    def on_draw(self):
        self.clear()
        # Obtener estados actualizados de los semáforos
        traffic_light_states = {
            pos: self.city_map.get_traffic_light_state(pos)
            for pos in self.city_map.traffic_system.lights.keys()
        }
        # Renderizar con los estados actualizados
        self.renderer.draw_traffic_lights(traffic_light_states, self.intersections)
