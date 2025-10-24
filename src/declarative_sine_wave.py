# uses HoloViews to declaratively create and display a sine wave curve with Bokeh backend.

import numpy as np
import holoviews as hv
hv.extension('bokeh')

xs = np.linspace(0, np.pi*5, 150)
ys = np.cos(xs)  # Changed to cosine for variation
curve = hv.Curve((xs, ys)).opts(title="Cosine Wave", color="blue", width=700)
print(curve)
