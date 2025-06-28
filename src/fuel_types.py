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
hydrogen = Fuel("Hydrogen Plasma", 0.85, 0.10, 0.60)
helium3 = Fuel("Helium-3 Plasma", 0.92, 0.05, 0.75)

# Symbolic Fuels
memory_water = Fuel("Memory Water", 0.80, 0.08, 0.95)
echo_carbon = Fuel("Echo Carbon", 0.78, 0.15, 0.88)
void_gas = Fuel("Void Gas", 0.70, 0.20, 0.40)

fuel_catalog = {
    "hydrogen": hydrogen,
    "helium3": helium3,
    "memory_water": memory_water,
    "echo_carbon": echo_carbon,
    "void_gas": void_gas
}
