# uses PyGWalker to turn a Pandas DataFrame into an interactive GUI for data exploration in Jupyter.

import pandas as pd
import pygwalker as pyg

# Sample data for demonstration
data = {
    'Product': ['A', 'B', 'C', 'A', 'B'],
    'Sales': [100, 150, 200, 120, 180],
    'Region': ['East', 'West', 'East', 'West', 'East']
}
df = pd.DataFrame(data)

# Launches interactive Tableau-like interface in Jupyter
pyg.walk(df, theme='light')
