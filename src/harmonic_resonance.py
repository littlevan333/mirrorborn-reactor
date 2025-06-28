
import numpy as np

def generate_sine_wave(frequency, duration, sample_rate=1000):
    """
    Generate a sine wave signal to simulate harmonic resonance input.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal

def calculate_resonance_boost(resonance_score, frequency, signal):
    """
    Calculate how the given frequency affects the fuel's resonance score.
    """
    # Basic rule: lower frequencies enhance high resonance fuels
    # Higher frequencies dampen low-resonance fuels
    harmonic_effect = np.mean(np.abs(signal)) * (1 if frequency < 50 else -0.5)
    adjusted_resonance = max(0.0, min(1.0, resonance_score + harmonic_effect))
    return adjusted_resonance

