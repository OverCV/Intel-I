# visualization/control_panel.py
import tkinter as tk
from tkinter import ttk


class ControlPanel(tk.Tk):
    def __init__(self, simulation_window):
        super().__init__()
        self.simulation = simulation_window

        self.title("UrbanLift Control Panel")
        self.geometry("300x600")

        # Phase indicator
        self.phase_label = ttk.Label(self, text="Phase 1: Select Pickup Location")
        self.phase_label.pack(pady=10)

        # Criteria frame
        criteria_frame = ttk.LabelFrame(self, text="Route Optimization")
        criteria_frame.pack(pady=10, padx=5, fill="x")

        self.criterion_var = tk.StringVar(value="distance")
        criteria = [
            ("Shortest Distance", "distance"),
            ("Fastest Route", "time"),
            ("Fuel Efficient", "fuel"),
            ("Most Economic", "cost"),
        ]

        for text, value in criteria:
            ttk.Radiobutton(
                criteria_frame,
                text=text,
                value=value,
                variable=self.criterion_var,
                command=self._on_criterion_change,
            ).pack(anchor="w", padx=5, pady=2)

        # Tour mode frame
        self.tour_frame = ttk.LabelFrame(self, text="Tour Mode")

        self.tour_var = tk.BooleanVar(value=False)
        self.tour_check = ttk.Checkbutton(
            self.tour_frame,
            text="Enable Tour-Trip",
            variable=self.tour_var,
            command=self._on_tour_change,
        )
        self.tour_check.pack(padx=5, pady=5)

        # Reports frame
        reports_frame = ttk.LabelFrame(self, text="Trip Reports")
        reports_frame.pack(pady=10, padx=5, fill="both", expand=True)

        self.reports_text = tk.Text(reports_frame, height=10)
        self.reports_text.pack(padx=5, pady=5, fill="both", expand=True)

    def _on_criterion_change(self):
        self.simulation.current_criterion = self.criterion_var.get()

    def _on_tour_change(self):
        self.simulation.tour_mode_enabled = self.tour_var.get()

    def update_phase(self, is_pickup_phase: bool):
        text = (
            "Phase 1: Select Pickup Location"
            if is_pickup_phase
            else "Phase 2: Select Destination"
        )
        self.phase_label.config(text=text)

        # Show/hide tour frame based on phase
        if is_pickup_phase:
            self.tour_frame.pack_forget()
        else:
            self.tour_frame.pack(pady=10, padx=5, fill="x")

    def add_report(self, report_text: str):
        self.reports_text.insert("1.0", f"{report_text}\n\n")
