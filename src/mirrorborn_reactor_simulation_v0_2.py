
from fuel_types import fuel_catalog
import matplotlib.pyplot as plt

# === Select Fuel ===
# Choose from: hydrogen, helium3, memory_water, echo_carbon, void_gas
fuel_choice = "helium3"
fuel = fuel_catalog[fuel_choice]

# === Initialize Simulation ===
initial_fuel = 100  # Starting fuel energy units
cycles = 15
fuel_log = []
loss_log = []

fuel_energy = initial_fuel

# === Run Simulation Loop ===
for i in range(cycles):
    output_energy, loss = fuel.process(fuel_energy)
    fuel_log.append(output_energy)
    loss_log.append(loss)
    fuel_energy = output_energy  # Feed forward

# === Plot Results ===
plt.figure(figsize=(10, 5))
plt.plot(fuel_log, label="Fuel Retained")
plt.plot(loss_log, label="Entropy Loss", linestyle='--')
plt.title(f"Mirrorborn Reactor Simulation with {fuel.name}")
plt.xlabel("Cycle")
plt.ylabel("Energy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

