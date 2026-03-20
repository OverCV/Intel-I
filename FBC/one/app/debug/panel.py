import arcade


class DebugPanel:
    def __init__(self):
        self.logs = []
        self.max_logs = 10

    def log(self, message):
        self.logs.append(message)
        if len(self.logs) > self.max_logs:
            self.logs.pop(0)

    def draw(self, x, y):
        # Dibujar un fondo semitransparente
        arcade.draw_rectangle_filled(
            x + 150,
            y - 100,
            300,
            200,
            arcade.color.BLACK + (200,),  # Negro semitransparente
        )

        # Dibujar estado actual
        start_y = y
        arcade.draw_text(f"Phase: {self.sim_state}", x, start_y, arcade.color.WHITE, 12)
        start_y -= 20
        arcade.draw_text(
            f"Selected Vehicle: {self.selected_vehicle.id if self.selected_vehicle else 'None'}",
            x,
            start_y,
            arcade.color.WHITE,
            12,
        )

        # Dibujar logs
        start_y -= 20
        for log in self.logs:
            arcade.draw_text(log, x, start_y, arcade.color.WHITE, 10)
            start_y -= 15
