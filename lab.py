import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

C = 1e-6
L = 0.0056
R = 56 + 50 

# Define the system of ODEs
# state = [v, i]
def model(state, t):
    v, i = state
    dvdt = (1 / C) * i
    didt = -(R / L) * i - (1 / L) * v + (2 / L)
    return [dvdt, didt]

# Initial conditions and time points
initial_state = [0.0, 0.0]
t = 1e-6 * np.linspace(0, 1000, 4000)  # seconds (0 to 1000 us)

# Solve the ODE
solution = odeint(model, initial_state, t)

# Extract solutions
v = solution[:, 0]
i = solution[:, 1]

# Compute outputs
v1 = 2 - i * 50
v2 = i * (R - 50)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t * 1e6, v1, label='v1(t)')
plt.plot(t * 1e6, v2, label='v2(t)')
plt.xlabel('t (µs)')
plt.ylabel('volts')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()







































import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\taiya\Downloads\scopy2.csv"

# Read file
df = pd.read_csv(file_path, skiprows=8)

# Rename columns
df.columns = ["Sample", "Time", "CH1", "CH2"]

# Force numeric (coerce bad values to NaN)
df["Time"] = pd.to_numeric(df["Time"], errors="coerce")
df["CH1"] = pd.to_numeric(df["CH1"], errors="coerce")
df["CH2"] = pd.to_numeric(df["CH2"], errors="coerce")

# Remove bad rows
df = df.dropna()

# Convert to numpy (important fix)
t = df["Time"].to_numpy()
ch1 = df["CH1"].to_numpy()
ch2 = df["CH2"].to_numpy()

# Plot
plt.figure(figsize=(10,4))

plt.plot(t * 1e6, ch1, label="CH1")
plt.plot(t * 1e6, ch2, label="CH2")

plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.title("Oscilloscope Capture")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


