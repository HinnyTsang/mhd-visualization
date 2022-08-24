import sys
"""
    Main script for the MHD visualization project.
    currently working on VisIt v3.0.0 (Python 2.7)
"""
import os
import errno
import config
import setting

sys.path.append(config.visit_path) # path to functions from visit into the python
sys.path.append(config.visit_exec_path) # execution path of VisIt
sys.path.insert(1, config.plots_path) # execution path of plots
sys.path.insert(1, config.camera_path) # execution path of plots

import visit as vst
from plots import volume # for volume plot
from camera import camera # for animation or setting view points.

if __name__ == "__main__":

    # load the visit libraries.
    # !!! make sure that 'visit' is in the shell's code !!! 
    vst.Launch() 

    # check file extension, if it is a 'visit' file, treat it as a series of files.
    input_file_full_path = os.path.join(setting.input_file_path, setting.input_file_name)
    input_file_ext = os.path.splitext(input_file_full_path)[1]

    if not os.path.exists(input_file_full_path):
        raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), input_file_full_path)

    if input_file_ext == ".visit":
        input_file_names = open(input_file_full_path).readlines()
        input_file_names = [file.strip() for file in input_file_names]
    else:
        input_file_names = [setting.input_file_name]


    # Loop through all files.
    for input_file_id, input_file_name in enumerate(input_file_names):
        
        input_file_full_name = os.path.join(setting.input_file_path, input_file_name)
        
        if not os.path.exists(input_file_full_path):
            raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), input_file_full_name)

        # TODO read files.
        print "Reading file %s" % (input_file_full_name)


        if not vst.OpenDatabase(input_file_full_name, 0, "Pixie"):
            raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), input_file_full_name)

        # TODO plot the scalar field.
        for scalar_field_name in setting.plot_scalar_field_names:            
            print r"Plotting scalar field: %s" % (scalar_field_name)
            vst.AddPlot("Volume", scalar_field_name)
            volume_attr = vst.VolumeAttributes()
            volume.set_volume_plot(vst, volume_attr)
            vst.SetPlotOptions(volume_attr)

        # TODO plot vector field.
        for vector_field_x, vector_field_y, vector_field_z in setting.plot_vector_field_names:
            
            print r"Plotting scalar field: %s, %s, %s" % (vector_field_x, vector_field_y, vector_field_z)
            # TODO plot vector field.

        # TODO plot scatter points.
        # ----------------------------

        # ----------------------------
        
        # TODO camera setting
        if setting.animation == True:
            # TODO animation
            camera.set_animate(vst)
            pass
        else:
            # TODO set view points & camera angle.
            view = vst.GetView3D()
            camera.set_view(view)
            vst.SetView3D(view)


        # TODO draw the plots
        draw_plots_state = vst.DrawPlots()
        if draw_plots_state == 0: sys.exit("Couldn't generate plot")
        
        # TODO save output files
        # SaveWindowAttributes object for save file.
        save_window = vst.SaveWindowAttributes()

        # loading the user settings.
        save_window.format   = save_window.PNG
        save_window.fileName = os.path.join(setting.output_file_path, r"%s_%05d" % (setting.output_file_name, input_file_id))
        save_window.width    = setting.figure_width 
        save_window.height   = setting.figure_height
        save_window.screenCapture   = 0
        
        vst.SetSaveWindowAttributes(save_window)
        save_file_name = vst.SaveWindow()
        print r"%s saved." % (save_file_name)       
        
        # clear the current plot.
        vst.DeleteActivePlots()

    # close the viewer
    vst.Close()