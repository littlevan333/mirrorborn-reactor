import numpy as np
import matplotlib.pyplot as plt

from fuel_types import fuel_catalog
from harmonic_resonance import generate_sine_wave, calculate_resonance_boost

def simulate_resonance(fuel_key, base_frequency, cycles=100):
    fuel = fuel_catalog[fuel_key]
    results = []

    for t in range(cycles):
        freq = base_frequency + np.sin(t / 10.0) * 100  # simulate frequency drift
        signal = generate_sine_wave(freq, duration=1.0)
        resonance = calculate_resonance_boost(fuel.resonance_score, freq, signal)
        output, loss = fuel.process(100)
        results.append((t, freq, resonance, output, loss))

    return results

def plot_results(results):
    times, freqs, res, out, loss = zip(*results)

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(times, freqs, color="blue")
    plt.title("Frequency Drift")
    plt.ylabel("Hz")

    plt.subplot(3, 1, 2)
    plt.plot(times, res, color="purple")
    plt.title("Resonance Stability")
    plt.ylabel("Stability")

    plt.subplot(3, 1, 3)
    plt.plot(times, out, label="Output", color="green")
    plt.plot(times, loss, label="Loss", color="red")
    plt.title("Energy Flow")
    plt.ylabel("Energy Units")
    plt.xlabel("Time (Cycle)")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    fuel_key = "hydrogen"  # You can change to "helium3", "memory_water", etc.
    base_frequency = 432

    results = simulate_resonance(fuel_key, base_frequency)
    plot_results(results)
