# This script generates a smooth visualization of millions of data points using Datashader,
# creating a scatter plot of random points and rendering it as an image without browser lag.

import datashader as ds
import numpy as np
import pandas as pd
from datashader import transfer_functions as tf
from PIL import Image

num_points = 42_000
data = pd.DataFrame(
    {"coord_x": np.random.randn(num_points), "coord_y": np.random.randn(num_points)}
)
plot_canvas = ds.Canvas(plot_width=700, plot_height=700)

aggregation = plot_canvas.points(data, "coord_x", "coord_y")
shaded_img = tf.shade(aggregation, cmap=["lightgreen", "darkgreen"])
pil_image = shaded_img.to_pil()
pil_image.save("scatter_plot.png")
