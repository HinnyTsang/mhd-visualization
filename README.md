# MHD Visualization tools 

Python scripts to generate 3D animation / plot using [VisIt](https://visit-dav.github.io/visit-website/index.html).
VisIt version installed in Rivanna: VisIt v3.0.0 [(user manuel)](https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/cli_manual)

* Python 2.7 is needed. see [issue](https://github.com/visit-dav/visit/issues/4648).

<!-- ## Test file
./scorpio-out/g1040_0021.h5 -->

## Input file format (Right Now):
- HDF5

## Overall Design
- `main.py`
- `setting.py`   --- I/O setting & plot settings
- `config.py` --- The environment path settings.
- `plot_volume.py` --- Plot scalar fields.
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


