# Uses HoloViews to declaratively create and 
# display a sine wave curve with Bokeh backend.

import holoviews as hv
import numpy as np

hv.extension("bokeh")

xs = np.linspace(0, np.pi * 5, 150)
ys = np.sin(xs)
curve = hv.Curve((xs, ys)).opts(title="Sine Wave", color="blue", width=700)

# Save to HTML file and open in browser
hv.save(curve, "sine_wave.html")
print("Sine wave plot saved to sine_wave.html and will open in browser...")

# Also display in browser
from bokeh.plotting import show
show(hv.render(curve))
