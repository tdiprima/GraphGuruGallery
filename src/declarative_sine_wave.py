# uses HoloViews to declaratively create and display a sine wave curve with Bokeh backend.

import holoviews as hv
import numpy as np

hv.extension("bokeh")

xs = np.linspace(0, np.pi * 5, 150)
ys = np.cos(xs)  # Changed to cosine for variation
curve = hv.Curve((xs, ys)).opts(title="Cosine Wave", color="blue", width=700)
print(curve)
