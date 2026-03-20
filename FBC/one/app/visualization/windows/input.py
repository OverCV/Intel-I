# app/visualization/windows/input.py
import arcade
from core.models.vehicle import VehicleState
from simulation.state import SimulationState
from visualization.windows.base import BaseWindow


class InputWindow(BaseWindow):
    """Maneja los inputs del usuario"""

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """Maneja clicks del mouse"""
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Primero verificar si es click en el panel de control
            if self.input_handler.handle_control_panel_click(self, x, y):
                return

            # Si no, procesar click en el mapa
            clicked_pos = self.input_handler.find_nearest_intersection(self, x, y)
            if clicked_pos:
                self._process_click(clicked_pos)

    def _process_click(self, clicked_pos):
        """Procesa un click según la fase actual"""
        if self.state_manager.state == SimulationState.PICKUP_PHASE:
            vehicle, route = self.input_handler.handle_pickup_click(self, clicked_pos)
            if vehicle and route:
                vehicle.route = route
                vehicle.state = VehicleState.PICKING_UP
                self.state_manager.switch_to_destination_phase(vehicle)
        else:
            route = self.input_handler.handle_destination_click(self, clicked_pos)
            if route:
                vehicle = self.state_manager.selected_vehicle
                vehicle.route = route
                vehicle.state = VehicleState.IN_TRIP

    def on_key_press(self, key, modifiers):
        """Maneja inputs de teclado"""
        self.input_handler.handle_key_press(self, key, modifiers)
