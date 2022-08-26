# -*- coding: utf-8 -*-
"""MHD Visualization

    Main script for the MHD visualization project.
    currently working on VisIt v3.0.0 (Python 2.7).
"""
from __future__ import print_function
import sys
import os
import errno
import setting
import visit as VisIt
from plots import volume, streamline
from camera import camera
from save import save
from read_data import read_h5_file, read_visit_file



if __name__ == "__main__":

    # load the visit libraries.
    # !!! make sure that 'visit' is in the shell's code !!!
    VisIt.Launch()
    print("Launched")
    # Check the plotting mode.
    if setting.CAMERA_MODE == 1:
        # TODO 1. fix camera, time evolve
        # STEP 1: Read file
        try:
            read_visit_file(setting.INPUT_FILE_PATH, setting.INPUT_FILE_NAME, VisIt)
        except OSError as err:
            print(err)

        # STEP 2. Plot the desired fields.
        for scalar_field in setting.PLOT_SCALAR_FIELD_NAMES:
            print(r"Plotting scalar field: %s" % scalar_field)
            volume.set_volume_plot(VisIt, scalar_field)

        for vector_field in setting.PLOT_VECTOR_FIELD_NAMES:
            print(r"Plotting vector field: %s" % vector_field)
            streamline.set_stream_plot(VisIt, vector_field)

        # STEP 3: Set camera angle.
        camera.set_view(VisIt)

        # STEP 4: Draw the plot.
        draw_plot_state = VisIt.DrawPlots()
        if draw_plot_state == 0:
            sys.exit("Couldn't generate plot.")

        # STEP 5: Save the picture.
        save.save_time_evolve(VisIt, setting)


    elif setting.CAMERA_MODE == 2:
        # TODO 2. moving camera, sngle snapshot
        pass

    elif setting.CAMERA_MODE == 3:
        # TODO 3. moving camera, time evolve
        # STEP 1. Read file
        try:
            read_visit_file(setting.INPUT_FILE_PATH, setting.INPUT_FILE_NAME, VisIt)
        except OSError:
            exit()
        pass

    elif setting.CAMERA_MODE == 4:
        # MODE 4. fix camera, single snapshopt
        # STEP 1. Read file
        try:
            read_h5_file(setting.INPUT_FILE_PATH, setting.INPUT_FILE_NAME, VisIt)
        except OSError as err:
            print ("{0}".format(err))
            exit()

        # STEP 2. Plot the desired fields.
        for scalar_field in setting.PLOT_SCALAR_FIELD_NAMES:
            print(r"Plotting scalar field: %s" % scalar_field)
            volume.set_volume_plot(VisIt, scalar_field)

        for vector_field in setting.PLOT_VECTOR_FIELD_NAMES:
            print(r"Plotting vector field: %s" % vector_field)
            streamline.set_stream_plot(VisIt, vector_field)

        # STEP 3: Set camera angle.
        camera.set_view(VisIt)

        # STEP 4: Draw the plot.
        draw_plot_state = VisIt.DrawPlots()
        if draw_plot_state == 0:
            sys.exit("Couldn't generate plot.")

        # STEP 5: Save the picture.
        save.save_snapshot(VisIt, setting)

    else:
        raise ValueError("CAMERA_MODE should be any of the following: 1, 2, 3, 4")

    # clear the current plot.
    VisIt.DeleteActivePlots()
    # close the viewer
    VisIt.Close()
