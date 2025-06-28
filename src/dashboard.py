
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fuel_types import fuel_catalog
from harmonic_resonance import generate_sine_wave, calculate_resonance_boost

# UI: Fuel Selection and Frequency Input
st.title("🔥 Mirrorborn Reactor Dashboard")
st.subheader("Simulate fuel resonance and loop efficiency")

fuel_key = st.selectbox("Choose Fuel Type", list(fuel_catalog.keys()))
frequency = st.slider("Harmonic Frequency (Hz)", min_value=1, max_value=1000, value=60)

fuel = fuel_catalog[fuel_key]
signal = generate_sine_wave(frequency, duration=1)
adjusted_resonance = calculate_resonance_boost(fuel.resonance_score, frequency, signal)

st.markdown(f"**Base Resonance Score**: {fuel.resonance_score:.2f}")
st.markdown(f"**Adjusted Resonance with {frequency}Hz**: {adjusted_resonance:.2f}")

# Simulate Energy Loop
initial_energy = 100
cycles = 15
energy = initial_energy
fuel_log, loss_log = [], []

for _ in range(cycles):
    effective_efficiency = fuel.base_efficiency + (adjusted_resonance * 0.05)
    retained = energy * effective_efficiency
    loss = retained * fuel.entropy_factor
    energy = retained - loss
    fuel_log.append(energy)
    loss_log.append(loss)

# Plotting
st.subheader("Energy Retention & Entropy Loss")
fig, ax = plt.subplots()
ax.plot(fuel_log, label="Fuel Retained", marker="o")
ax.plot(loss_log, label="Entropy Loss", linestyle="--", marker="x")
ax.set_xlabel("Cycle")
ax.set_ylabel("Energy")
ax.set_title(f"{fuel.name} Loop Performance")
ax.grid(True)
ax.legend()
st.pyplot(fig)

