# MHD Visualization tools 

Python scripts to generate 3D animation / plot using [VisIt](https://visit-dav.github.io/visit-website/index.html).


## Input file format:
- HDF5

## Overall Design
- main.py
- read_file.py  --- convert file to the format used in the plot
- setting.py   --- customize the plot / animation
- plot.py --- mode of output
- animation.py --- mode of output
- iso_surface --- plot scalar field
  - iso_surface.py
  - color_pallete.py
- stream_line --- plot vector field
  - stream_line.py
  - color_pallete.py
  - density.py
  - seed.py

## Cooding style
Follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
