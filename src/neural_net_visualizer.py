# Generates a simple neural network diagram using matplotlib
# This is a Python-based alternative to PlotNeuralNet (which uses LaTeX)

from pathlib import Path

import matplotlib.pyplot as plt
import yaml
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# Sample YAML config
config = """
layers:
  - type: Input
    shape: [28, 28, 1]
  - type: Conv2D
    filters: 32
    kernel: [3, 3]
  - type: MaxPool2D
    pool: [2, 2]
  - type: Dense
    units: 10
connections:
  - from: Input
    to: Conv2D
  - from: Conv2D
    to: MaxPool2D
  - from: MaxPool2D
    to: Dense
"""

Path("simple_cnn.yaml").write_text(config)

# Parse the YAML config
with open("simple_cnn.yaml", "r") as f:
    nn_config = yaml.safe_load(f)

# Create visualization
fig, ax = plt.subplots(figsize=(14, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# Layer positions and colors
layer_colors = {
    "Input": "#E8F4F8",
    "Conv2D": "#B8E6F0",
    "MaxPool2D": "#7FC8E0",
    "Dense": "#4A90A4",
}

# Draw layers
x_positions = [1, 3, 5, 7]
layers = nn_config["layers"]

for i, (layer, x_pos) in enumerate(zip(layers, x_positions)):
    layer_type = layer["type"]
    color = layer_colors.get(layer_type, "#CCCCCC")

    # Create layer box
    if layer_type == "Input":
        label = f"{layer_type}\n{layer['shape']}"
    elif layer_type == "Conv2D":
        label = f"{layer_type}\nFilters: {layer['filters']}\nKernel: {layer['kernel']}"
    elif layer_type == "MaxPool2D":
        label = f"{layer_type}\nPool: {layer['pool']}"
    elif layer_type == "Dense":
        label = f"{layer_type}\nUnits: {layer['units']}"
    else:
        label = layer_type

    # Draw fancy box
    box = FancyBboxPatch(
        (x_pos - 0.4, 2),
        0.8,
        2,
        boxstyle="round,pad=0.1",
        edgecolor="black",
        facecolor=color,
        linewidth=2,
    )
    ax.add_patch(box)

    # Add text
    ax.text(x_pos, 3, label, ha="center", va="center", fontsize=9, weight="bold")

# Draw connections
for i in range(len(layers) - 1):
    x_start = x_positions[i] + 0.4
    x_end = x_positions[i + 1] - 0.4
    arrow = FancyArrowPatch(
        (x_start, 3),
        (x_end, 3),
        arrowstyle="->",
        mutation_scale=20,
        linewidth=2,
        color="#333333",
    )
    ax.add_patch(arrow)

plt.title("Neural Network Architecture (CNN)", fontsize=16, weight="bold", pad=20)
plt.tight_layout()
plt.savefig("cnn_diagram.png", dpi=300, bbox_inches="tight")
print("Neural network diagram saved as 'cnn_diagram.png'")
plt.show()
