# app/visualization/windows/render.py
import arcade
from simulation.state import SimulationState
from config.consts import SCREEN_HEIGHT, SCREEN_WIDTH
from visualization.windows.base import BaseWindow


class RenderWindow(BaseWindow):
    def on_draw(self):
        self.clear()
        self._draw_simulation()
        self._draw_control_panel()

    def _draw_simulation(self):
        arcade.draw_xywh_rectangle_filled(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.WHITE
        )
        self.renderer.draw_all(
            self.intersections,
            self.city_map.traffic_system,
            self.vehicle_manager.vehicles,
            self.state_manager.selected_vehicle,
            self.bus_stops,
        )

    def _draw_control_panel(self):
        start_x = SCREEN_WIDTH + 20
        current_y = SCREEN_HEIGHT - 40

        # Phase indicator
        arcade.draw_text(
            f"Phase: {self.state_manager.state.value}",
            start_x,
            current_y,
            arcade.color.BLACK,
            18,
            bold=True,
        )

        # Route Optimization section
        current_y -= 60
        arcade.draw_text(
            "Route Optimization", start_x, current_y, arcade.color.BLACK, 16, bold=True
        )

        # Criterios con radio buttons
        criteria = [
            ("Shortest Distance", "distance"),
            ("Fastest Route", "time"),
            ("Fuel Efficient", "fuel"),
            ("Most Economic", "cost"),
        ]

        for text, value in criteria:
            current_y -= 30
            # Dibujar círculo de selección (radio button)
            arcade.draw_circle_outline(
                start_x + 10, current_y + 8, 8, arcade.color.BLACK, 1
            )
            # Si está seleccionado, dibujar círculo interior
            if value == self.state_manager.current_criterion:
                arcade.draw_circle_filled(
                    start_x + 10, current_y + 8, 4, arcade.color.BLACK
                )

            # Texto del criterio
            arcade.draw_text(text, start_x + 25, current_y, arcade.color.BLACK, 14)

        # Tour Mode checkbox (solo en fase de destino)
        if self.state_manager.state == SimulationState.DESTINATION_PHASE:
            current_y -= 50
            arcade.draw_text(
                "Tour Mode", start_x, current_y, arcade.color.BLACK, 16, bold=True
            )

            current_y -= 30
            # Checkbox
            arcade.draw_rectangle_outline(
                start_x + 10, current_y + 8, 16, 16, arcade.color.BLACK, 1
            )
            if self.state_manager.tour_mode_enabled:
                arcade.draw_text(
                    "✓", start_x + 5, current_y + 2, arcade.color.BLACK, 14, bold=True
                )

            arcade.draw_text(
                "Enable Tour-Trip", start_x + 35, current_y, arcade.color.BLACK, 14
            )

        # Estado de simulación
        current_y -= 40
        arcade.draw_text(
            f"{'PAUSED' if self.paused else 'RUNNING'}",
            start_x,
            current_y,
            arcade.color.RED if self.paused else arcade.color.GREEN,
            14,
            bold=True,
        )

        # Velocidad
        current_y -= 20
        arcade.draw_text(
            f"Speed: x{self.simulation_speed:.1f}",
            start_x,
            current_y,
            arcade.color.BLACK,
            14,
        )

        # Vehículo seleccionado
        if self.state_manager.selected_vehicle:
            current_y -= 40
            vehicle = self.state_manager.selected_vehicle
            arcade.draw_text(
                f"Selected: {vehicle.id}",
                start_x,
                current_y,
                arcade.color.BLACK,
                14,
            )
            current_y -= 20
            arcade.draw_text(
                f"State: {vehicle.state.value}",
                start_x,
                current_y,
                arcade.color.BLACK,
                14,
            )
