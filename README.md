## 🐍 Python Visualization Libraries Lab

![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

Welcome to the lab where code meets ✨aesthetic✨.

This repo is packed with examples and remixed snippets from some of Python's coolest visualization libraries — like PyWaffle, Lux, HoloViews, Datashader, PlotNeuralNet, VizTracer, and PyGWalker.

### 🎯 Purpose

We're here to make data *look good* and code *make sense*.  
Each file shows off a different way to visualize your work — complete with a quick header comment to tell you what's going on.

### ⚙️ How to Use

* Run each Python file in your own setup (Jupyter notebooks are 💯 for the interactive stuff).
* Swap out file paths or data as needed.
* Tinker, test, and make it your own.

### 📊 What We Learned

**Lux Visualization Issues (Python 3.13)**

We tried using Lux for automatic DataFrame visualizations, but ran into compatibility issues:

- JavaScript widgets don't render properly in newer Jupyter environments
- Toggle button appears but doesn't function
- Date parsing warnings on non-date columns

**Alternative Libraries Tested:**

✅ **Working:**

- **Plotly Express** - Reliable, interactive, lightweight
- **YData Profiling** - Comprehensive automated EDA reports
- ~~**D-Tale** - Interactive data explorer with Flask backend~~
- **Sweetviz** - Beautiful HTML comparison reports
- **Pandas built-in plotting** - Always available, no extra deps

❌ **Also Had Issues:**

- **Lux** - Widget compatibility problems with Python 3.13/newer Jupyter

**Recommendation:** Use Plotly Express for interactive visualizations or YData Profiling for comprehensive automated analysis. Both work with Python 3.13+.

See `auto_visualize_alternatives.ipynb` for working examples.

### 💡 Contributions

Got a cooler example or a creative tweak? Fork it, PR it, and show us what you've got! 🚀
