# creates a waffle chart using PyWaffle to visualize programming language popularity as percentages in a grid format.

import matplotlib.pyplot as plt
from pywaffle import Waffle

data = {"Python": 52, "JavaScript": 24, "Java": 14, "Other": 10}

fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=data,
    labels=[f"{k} ({v}%)" for k, v in data.items()],
    legend={"loc": "upper right", "bbox_to_anchor": (1.1, 1)},
)
plt.show()
