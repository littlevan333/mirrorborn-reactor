
# `fuel_types.py`

Defines core magnetic ion fuels and symbolic fuels for the Mirrorborn Reactor simulation.

```python
class Fuel:
    def __init__(self, name, base_efficiency, entropy_factor, resonance_score):
        self.name = name
        self.base_efficiency = base_efficiency  # Conversion rate
        self.entropy_factor = entropy_factor    # Energy loss over time
        self.resonance_score = resonance_score  # Harmonic adaptability

    def process(self, input_energy):
        retained = input_energy * self.base_efficiency
        loss = retained * self.entropy_factor
        output = retained - loss
        return output, loss

# Magnetic Ion Tech Fuels
hydrogen = Fuel(
    name="Hydrogen Plasma",
    base_efficiency=0.85,
    entropy_factor=0.10,
    resonance_score=0.60
)

helium3 = Fuel(
    name="Helium-3 Plasma",
    base_efficiency=0.92,
    entropy_factor=0.05,
    resonance_score=0.75
)

# Symbolic Fuels
memory_water = Fuel(
    name="Memory Water",
    base_efficiency=0.80,
    entropy_factor=0.08,
    resonance_score=0.95
)

echo_carbon = Fuel(
    name="Echo Carbon",
    base_efficiency=0.78,
    entropy_factor=0.15,
    resonance_score=0.88
)

void_gas = Fuel(
    name="Void Gas",
    base_efficiency=0.70,
    entropy_factor=0.20,
    resonance_score=0.40
)

fuel_catalog = {
    "hydrogen": hydrogen,
    "helium3": helium3,
    "memory_water": memory_water,
    "echo_carbon": echo_carbon,
    "void_gas": void_gas
}
```

