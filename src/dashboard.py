import streamlit as st
import matplotlib.pyplot as plt

from fuel_types import fuel_catalog
from harmonic_resonance import calculate_resonance_boost as calculate_resonance

st.title("🔁 Mirrorborn Reactor UI")

# Fuel selector
fuel_name = st.selectbox("Select Fuel Type", list(fuel_catalog.keys()))
fuel = fuel_catalog[fuel_name]

# Frequency slider
frequency = st.slider("Frequency (Hz)", 100, 1000, 432)

# Calculate resonance
resonance = calculate_resonance(frequency)
st.metric(label="Resonance Stability", value=f"{resonance:.3f}")

# Simulate energy processing
input_energy = 100
output, loss = fuel.process(input_energy)

st.write(f"🔥 Processed `{fuel.name}`")
st.write(f"⚡ Output Energy: {output:.2f}")
st.write(f"🧊 Entropy Loss: {loss:.2f}")

# Simple resonance graph
fig, ax = plt.subplots()
ax.plot([frequency], [resonance], 'ro')
ax.set_xlim(100, 1000)
ax.set_ylim(0, 1.1)
ax.set_title("Resonance vs Frequency")
ax.set_xlabel("Hz")
ax.set_ylabel("Resonance")
st.pyplot(fig)
