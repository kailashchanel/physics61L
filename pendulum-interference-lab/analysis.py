import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data_files = ["data1.csv", "data2.csv", "data3.csv", "data4.csv", "data5.csv"]
gravities_w_error = []
gravities = []

for i, file in enumerate(data_files):
    # Load the CSV data
    data = pd.read_csv(file)

    # Extract columns
    x = data['x']
    y = data['y']
    t = data['t']

    # Identify Peaks and Calculate Period for Damped Pendulum
    peaks, _ = find_peaks(x)
    t_peaks = t[peaks]
    time_intervals = np.diff(t_peaks)  # Time differences between peaks

    # Calculate frequency and period
    periods = time_intervals
    mean_period = np.mean(periods)

    # Measure g from Period and Length of Pendulum
    def measure_g(lengths, periods):
        g_values = (4 * np.pi**2 * lengths) / (periods ** 2)
        return np.mean(g_values), np.std(g_values)

    # Example pendulum lengths (in meters)
    lengths = np.array([0.7]) # 0.7m pendulum length used in experiment

    g_mean, g_std = measure_g(lengths, mean_period)
    print(f"Measured g: {g_mean:.4f} m/s² ± {g_std:.4f}")
    gravities_w_error.append(f"{g_mean:.4f} m/s² ± {g_std:.4f}")
    gravities.append(g_mean)

    # Generate position vs time plots in x and y dimensions
    plt.figure(figsize=(10, 6))
    plt.plot(t, x, marker='o', linestyle='-', color='g')
    plt.title(f"Position (x) vs Time ({str(i+1)})")
    plt.xlabel('Time (t)')
    plt.ylabel('x (m)')
    plt.grid(True)
    plt.savefig(f"plots/position-x-vs-time-{str(i+1)}")


    plt.figure(figsize=(10, 6))
    plt.plot(t, y, marker='o', linestyle='-', color='y')
    plt.title(f"Position (y) vs Time ({str(i+1)})")
    plt.xlabel('Time (t)')
    plt.ylabel('y (m)')
    plt.grid(True)
    plt.savefig(f"plots/position-y-vs-time-{str(i+1)}")

    # Find peaks in the 'x' column (sinusoidal wave)
    peaks, _ = find_peaks(x)

    # Get the times corresponding to the peaks
    t_peaks = t[peaks]

    # Calculate the time differences between consecutive peaks (to calculate frequency)
    time_intervals = np.diff(t_peaks)

    # Calculate the frequency (1/time_interval)
    frequency = 1 / time_intervals

    # Plot the frequency against time
    # The frequency is between peaks, so we plot it at the midpoint of the time intervals
    t_midpoints = t_peaks[:-1] + np.diff(t_peaks) / 2

    plt.figure(figsize=(10, 6))
    plt.plot(t_midpoints, frequency, marker='o', linestyle='-', color='r')
    plt.title(f"Frequency vs Time ({str(i+1)})")
    plt.xlabel('Time (t)')
    plt.ylabel('Frequency (1/s)')
    plt.grid(True)
    plt.savefig(f"plots/rate-of-change-of-frequency-vs-time-{str(i+1)}")

    # Calculate the rate of change of frequency (derivative of frequency)
    frequency_change_rate = np.diff(frequency) / np.diff(t_peaks[:-1])

    # Plot the rate of change of frequency against time (t)
    plt.figure(figsize=(10, 6))
    plt.plot(t_peaks[1:-1], frequency_change_rate, marker='o', linestyle='-', color='b')
    plt.title(f"Rate of Change of Frequency vs Time ({str(i+1)})")
    plt.xlabel('Time (t)')
    plt.ylabel('Rate of Change of Frequency (1/s²)')
    plt.grid(True)
    plt.savefig(f"plots/frequency-vs-time-{str(i+1)}")


df = pd.DataFrame({"Experimentally Calculated Gravitational Acceleration (g)": gravities_w_error})
df.to_csv("plots/gravities.csv", index=False)