import sys
"""
    Main script for the MHD visualization project.
    currently working on VisIt v3.0.0 (Python 2.7)
"""
import os
import config
import setting

sys.path.append(config.visit_path) # path to functions from visit into the python
sys.path.append(config.visit_exec_path) # execution path of VisIt

import visit as vst
from plot_volume import set_volume_plot

if __name__ == "__main__":

    # load the visit libraries.
    # !!! make sure that 'visit' is in the shell's code !!! 
    vst.Launch() 

    # TODO read files.
    vst.OpenDatabase(os.path.join(setting.input_file_path, setting.input_file_name))


    # TODO plot the scalar field.
    if len(setting.plot_scalar_field_names) > 0:
        
        for scalar_field_name in setting.plot_scalar_field_names:
            
            print r"Plotting scalar field: %s" % (scalar_field_name)

            # print vst.OperatorPlugins()

            # volume plot.
            vst.AddPlot("Volume", scalar_field_name)
            volume_attr = vst.VolumeAttributes()
            set_volume_plot(vst, volume_attr)
            vst.SetPlotOptions(volume_attr)

            # pseudocolor plot.
            # vst.AddOperator("Isosurface")
            
            # pseudocolor_attr = vst.PseudocolorAttributes()
            # pseudocolor_attr.colorTableName = "rainbow"
            # pseudocolor_attr.opacity = 0.1
            # vst.SetPlotOptions(pseudocolor_attr)


            # isosurface_attr = vst.IsosurfaceAttributes()
            # # isosurface_attr.opacity = 0.5
            # vst.SetOperatorOptions(isosurface_attr)


            # vst.AddPlot("Pseudocolor", scalar_field_name)
            # pseudocolor_attr.colorTableName = "rainbow"
            # pseudocolor_attr.opacity = 0.1     
            # vst.SetPlotOptions(pseudocolor_attr)

            # draw all plots  
            draw_plots_state = vst.DrawPlots()



            if draw_plots_state == 0:
                print "Couldn't generate plot"
                sys.exit()
            

    # TODO plot vector field.

    # TODO plot scatter points.

    # TODO save output files
    # SaveWindowAttributes object for save file.
    save_window = vst.SaveWindowAttributes()

    # loading the user settings.
    save_window.format   = save_window.PNG
    save_window.fileName = os.path.join(setting.output_file_path, setting.output_file_name)
    save_window.width    = setting.figure_width 
    save_window.height   = setting.figure_height
    save_window.screenCapture   = 0
    
    vst.SetSaveWindowAttributes(save_window)
    save_file_name = vst.SaveWindow()

    # close the viewer
    vst.Close()
    print r"%s saved." % (save_file_name)