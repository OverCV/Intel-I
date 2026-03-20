from enum import Enum


class SimulationState(Enum):
    PICKUP_PHASE = "pickup"  # Fase 1: Selección punto recogida
    DESTINATION_PHASE = "destination"  # Fase 2: Selección destino


class SimulationStateManager:
    def __init__(self):
        self.state = SimulationState.PICKUP_PHASE  # cambiar sim_state a state
        self.selected_vehicle = None
        self.tour_mode_enabled = False
        self.current_criterion = "distance"

    def switch_to_destination_phase(self, vehicle):
        self.selected_vehicle = vehicle
        self.state = SimulationState.DESTINATION_PHASE

    def reset_to_pickup_phase(self):
        self.selected_vehicle = None
        self.state = SimulationState.PICKUP_PHASE
