import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis with a gray background
fig, ax = plt.subplots()
ax.set_facecolor('#2B2B2B')  # Grayish background color
fig.patch.set_facecolor('#2B2B2B')  # Match the figure color to the axis color

x = np.linspace(0, 10, 1000)
y = np.sin(x)

# Plot the data with a cyan line
ax.plot(x, y, color='cyan', linewidth=2)

# Set title and labels for axes with white color
ax.set_title("Beautiful Sine Wave on Gray Background", color='white')
ax.set_xlabel("X", color='white')
ax.set_ylabel("sin(X)", color='white')

# Set the tick colors to white
ax.tick_params(colors='white')

# Add gridlines
ax.grid(True, linestyle='--', linewidth=0.5, color='white', alpha=0.6)

# Display the plot
plt.show()
