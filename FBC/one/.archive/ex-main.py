
# from typing import Optional
# import numpy as np
# import arcade
# import math

# from logic import CityMap, TrafficLightState, Vehicle, VehicleState

# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 800
# SCREEN_TITLE = "UrbanLift Simulation"

# # Colors
# ROAD_COLOR = arcade.color.DARK_GRAY
# VEHICLE_COLOR = arcade.color.YELLOW
# TRAFFIC_LIGHT_RED = arcade.color.RED
# TRAFFIC_LIGHT_GREEN = arcade.color.GREEN
# TRAFFIC_LIGHT_YELLOW = arcade.color.YELLOW
# BUS_STOP_COLOR = arcade.color.BLUE


# class SimulationWindow(arcade.Window):
#     def __init__(self):
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#         arcade.set_background_color(arcade.color.WHITE)

#         # Initialize simulation components
#         self.city_map = CityMap()  # Esta es la conexión entre las capas
#         self.vehicles = {}
#         self.traffic_lights = {}
#         self.bus_stops = []

#         # Simulation state
#         self.paused = False
#         self.simulation_speed = 1.0

#     def setup(self):
#         """Set up the simulation."""
#         # Create the city map 10x10 (grid-based for simplicity)
#         self.create_grid_map(10, 10)
#         # Crear algunos vehículos de prueba
#         self.add_test_vehicles(3)



#     def create_grid_map(self, rows: int, cols: int):
#         """Create a grid-based city map."""
#         cell_width = SCREEN_WIDTH / (cols + 1)
#         cell_height = SCREEN_HEIGHT / (rows + 1)

#         # Create intersections dictionary for visualization
#         self.intersections = {}

#         # First create all intersections
#         for row in range(rows):
#             for col in range(cols):
#                 x = (col + 1) * cell_width
#                 y = (row + 1) * cell_height
#                 pos = (x, y)
#                 self.intersections[(col, row)] = pos

#                 # Add traffic lights at alternating intersections
#                 if (row + col) % 2 == 0:
#                     self.city_map.add_traffic_light(pos, cycle_time=30)
#                     self.traffic_lights[(col, row)] = TrafficLightState.RED

#         # Then create all streets (connections between intersections)
#         for row in range(rows):
#             for col in range(cols):
#                 current_pos = self.intersections[(col, row)]

#                 # Add horizontal connections
#                 if col < cols - 1:
#                     next_pos = self.intersections[(col + 1, row)]
#                     self.city_map.add_street(current_pos, next_pos, direction="both")

#                 # Add vertical connections
#                 if row < rows - 1:
#                     next_pos = self.intersections[(col, row + 1)]
#                     self.city_map.add_street(current_pos, next_pos, direction="both")

#         # Add bus stops along the diagonal
#         for i in range(min(rows, cols)):
#             pos = self.intersections[(i, i)]
#             self.city_map.add_bus_stop(pos)
#             self.bus_stops.append(pos)

#     def on_draw(self):
#         """Render the screen."""
#         self.clear()

#         # Draw roads
#         self.draw_roads()

#         # Draw traffic lights
#         self.draw_traffic_lights()

#         # Draw vehicles
#         self.draw_vehicles()

#         # Draw bus stops
#         self.draw_bus_stops()

#     def draw_roads(self):
#         """Draw the road network."""
#         for (col1, row1), (x1, y1) in self.intersections.items():
#             for (col2, row2), (x2, y2) in self.intersections.items():
#                 # Draw horizontal and vertical roads only
#                 if (abs(col1 - col2) == 1 and row1 == row2) or (
#                     abs(row1 - row2) == 1 and col1 == col2
#                 ):
#                     arcade.draw_line(x1, y1, x2, y2, ROAD_COLOR, 3)

#     def draw_traffic_lights(self):
#         """Draw all traffic lights."""
#         for (col, row), state in self.traffic_lights.items():
#             x, y = self.intersections[(col, row)]
#             color = (
#                 TRAFFIC_LIGHT_RED
#                 if state == TrafficLightState.RED
#                 else TRAFFIC_LIGHT_GREEN
#                 if state == TrafficLightState.GREEN
#                 else TRAFFIC_LIGHT_YELLOW
#             )
#             arcade.draw_circle_filled(x, y, 5, color)

#     def draw_vehicles(self):
#         """Draw all vehicles."""
#         for vehicle_id, vehicle in self.vehicles.items():
#             x, y = vehicle.position
#             arcade.draw_circle_filled(x, y, 8, VEHICLE_COLOR)
#             # Draw vehicle ID
#             arcade.draw_text(vehicle_id, x - 10, y + 10, arcade.color.BLACK, 8)

#     def draw_bus_stops(self):
#         """Draw all bus stops."""
#         for x, y in self.bus_stops:
#             arcade.draw_rectangle_filled(x, y, 10, 10, BUS_STOP_COLOR)

#     def update(self, delta_time: float):
#         """Update simulation state."""
#         if not self.paused:
#             # Update traffic lights
#             self.update_traffic_lights(delta_time * self.simulation_speed)

#             # Update vehicle positions
#             self.update_vehicles(delta_time * self.simulation_speed)

#     def update_traffic_lights(self, delta_time: float):
#         """Update traffic light states."""
#         for pos in self.traffic_lights:
#             # Simple traffic light cycle
#             if np.random.random() < 0.01:  # Random state change for demonstration
#                 current_state = self.traffic_lights[pos]
#                 self.traffic_lights[pos] = self.next_traffic_light_state(current_state)

#     def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
#         """Handle mouse clicks"""
#         if button == arcade.MOUSE_BUTTON_LEFT:
#             # Encontrar la intersección más cercana al clic
#             destination = self.find_nearest_intersection(x, y)

#             # Encontrar el vehículo disponible más cercano
#             vehicle_id = self.find_nearest_vehicle(destination)

#             if vehicle_id:
#                 # Mover el vehículo al destino
#                 self.move_vehicle_to(vehicle_id, destination)

#     def request_vehicle(self, x, y):
#         """Procesar una nueva solicitud de vehículo"""
#         # 1. Encontrar la intersección más cercana al clic
#         pickup_point = self.find_nearest_intersection(x, y)

#         # 2. Encontrar el vehículo más cercano disponible
#         vehicle = self.find_nearest_available_vehicle(pickup_point)

#         if vehicle:
#             # 3. Calcular ruta óptima hasta el pasajero
#             pickup_route = self.city_map.find_shortest_path(
#                 vehicle.position, pickup_point, criterion="time"
#             )

#             # 4. Asignar la ruta al vehículo
#             vehicle.route = pickup_route


#     def update_vehicles(self, delta_time: float):
#         """Update vehicle positions."""
#         for vehicle in self.vehicles.values():
#             if vehicle.route:
#                 # Obtener el siguiente punto de la ruta
#                 next_point = vehicle.route[0]

#                 # Calcular distancia al siguiente punto
#                 dx = next_point[0] - vehicle.position[0]
#                 dy = next_point[1] - vehicle.position[1]
#                 distance = math.sqrt(dx * dx + dy * dy)

#                 if distance < 2.0:  # Si está muy cerca, considerar que llegó
#                     vehicle.position = next_point
#                     vehicle.route.pop(0)  # Remover el punto alcanzado

#                     # Si la ruta está vacía, llegó al destino
#                     if not vehicle.route:
#                         vehicle.state = VehicleState.IDLE
#                         vehicle.destination = None
#                 else:
#                     # Mover hacia el siguiente punto
#                     speed = vehicle.speed * delta_time * self.simulation_speed
#                     ratio = speed / distance
#                     new_x = vehicle.position[0] + dx * ratio
#                     new_y = vehicle.position[1] + dy * ratio
#                     vehicle.position = (new_x, new_y)

#     def next_traffic_light_state(
#         self, current_state: TrafficLightState
#     ) -> TrafficLightState:
#         """Get the next state for a traffic light."""
#         if current_state == TrafficLightState.RED:
#             return TrafficLightState.GREEN
#         elif current_state == TrafficLightState.GREEN:
#             return TrafficLightState.YELLOW
#         else:
#             return TrafficLightState.RED

#     def on_key_press(self, key, modifiers):
#         """Handle key press events."""
#         if key == arcade.key.SPACE:
#             self.paused = not self.paused
#         elif key == arcade.key.UP:
#             self.simulation_speed *= 1.5
#         elif key == arcade.key.DOWN:
#             self.simulation_speed /= 1.5


# def main():
#     window = SimulationWindow()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()
