# MHD Visualization tools 

Python scripts to generate 3D animation / plot using [VisIt](https://visit-dav.github.io/visit-website/index.html).
VisIt version installed in Rivanna: VisIt v3.0.0 [(user manuel)](https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/cli_manual)

* Python 2.7 is needed. see [issue](https://github.com/visit-dav/visit/issues/4648).

<!-- ## Test file
./scorpio-out/g1040_0021.h5 -->

## Input file format (Right Now):
- `.h5` (HDF5)
- `.athdf` (HDF5) with `.athdf.xdmf` (must included if AMR is included in the simulation, see [Athena++](https://github.com/PrincetonUniversity/athena/wiki/SMR-and-AMR)).


## Time Evolution of Single Simulation

To plot with time evolution, Athena++ creat a series of files, with following name pattern `<prefix>.hydro.<file_id>.athdf` & `<prefix>.hydro.<file_id>.athdf.xdmf`. Although VisIt could automatically group the files as a database, it is recommoned to create a `.visit` file which contains the list of files for the plot (see [VisIt docs](https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/gui_manual/Animation/Animation_basics.html#the-visit-file)). An example of `.visit` could be found in the `test` folder.

## Plotting Mode
1. Fix camera, time evolve.
2. Single snapshot, moving camera.
3. Moving Camera, time evolve.
4. Single snapshot, fixed camera.

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


