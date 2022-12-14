# MHD Visualization tools 

Python scripts to generate 3D animation / plot using [VisIt](https://visit-dav.github.io/visit-website/index.html).
VisIt version installed in Rivanna: VisIt v3.0.0 [(user manuel)](https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/cli_manual)

* Python 2.7 is required. see [issue](https://github.com/visit-dav/visit/issues/4648).

<!-- ## Test file
./scorpio-out/g1040_0021.h5 -->

## Input file format (Right Now):
- `.h5` (HDF5)
- `.athdf` (HDF5) with `.athdf.xdmf` (must included if AMR is included in the simulation, see [Athena++](https://github.com/PrincetonUniversity/athena/wiki/SMR-and-AMR)).


## Time Evolution of Single Simulation

To plot with time evolution, Athena++ creat a series of files, with following name pattern `<prefix>.hydro.<file_id>.athdf` & `<prefix>.hydro.<file_id>.athdf.xdmf`. Although VisIt could automatically group the files as a database, it is recommoned to create a `.visit` file which contains the list of files for the plot (see [VisIt docs](https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/gui_manual/Animation/Animation_basics.html#the-visit-file)). An example of `.visit` could be found in the `test` folder.

## Modes
1. fix camera, time evolve
2. moving camera, sngle snapshot
3. moving camera, time evolve
4. fix camera, single snapshopt

## File structure in `./src`
- `main.py`
- `setting.py`   --- I/O setting & plot settings
- `read_data.py` --- Read database to VisIt.
- `plots/` --- Setting for different plots.
  - `volume.py` --- volume plot for visualising scalar fields.
  - `streamline.py` --- streamline plit for visuzlising vector fields.
- `camera/` --- Setting for static/moving camera
  - `camera.py ` --- setting camera.
  - `default_track/` --- defult moving camera settings.
    - `rotation.py` --- setting for rotation around the $z$ axis.
- `save/`
  - `save.py`  --- setting for generating output

## Cooding style
Follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
