import tkinter as tk
from tkinter import messagebox


class FuelMeter:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Fuel Meter")

        # Settings
        self.max_fuel = 15
        self.current_fuel = self.max_fuel
        self.is_paused = False
        self.decrement_interval = 120000  # 2 minutes in milliseconds

        # Create fuel bars
        self.fuel_bars = []
        for i in range(self.max_fuel):
            color = "green" if i < 13 else "red"
            bar = tk.Frame(root, width=30, height=20, bg=color, relief="ridge", borderwidth=1)
            bar.grid(row=self.max_fuel - i - 1, column=0, padx=5, pady=2)
            self.fuel_bars.append(bar)

        # Instructions
        self.instructions = tk.Label(
            root, text="Single Tap: Pause/Play\nDouble Tap: Refill Fuel", font=("Arial", 12)
        )
        self.instructions.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Bind mouse actions
        root.bind("<Button-1>", self.handle_single_tap)  # Single tap (pause/play)
        root.bind("<Double-1>", self.handle_double_tap)  # Double tap (refill)

        # Start the fuel bar decrementing process
        self.update_fuel()

    def update_fuel(self):
        """Decrease fuel level every 2 minutes unless paused."""
        if not self.is_paused and self.current_fuel > 0:
            self.current_fuel -= 1
            self.update_fuel_bars()
        if self.current_fuel == 0:
            messagebox.showinfo("Fuel Meter", "Fuel is empty!")
        self.root.after(self.decrement_interval, self.update_fuel)

    def update_fuel_bars(self):
        """Update the visual representation of the fuel level."""
        for i in range(self.max_fuel):
            if i < self.current_fuel:
                self.fuel_bars[i].configure(bg="green" if i < 13 else "red")
            else:
                self.fuel_bars[i].configure(bg="gray")

    def handle_single_tap(self, event):
        """Pause or resume fuel consumption on single tap."""
        self.is_paused = not self.is_paused

    def handle_double_tap(self, event):
        """Refill fuel to maximum on double tap."""
        self.current_fuel = self.max_fuel
        self.update_fuel_bars()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FuelMeter(root)
    root.mainloop()
