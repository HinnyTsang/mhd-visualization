# -*- coding: utf-8 -*-
"""
    Save the plots.
"""
import os

def save_setting(VisIt, setting):
    """Save the plotting attributes.

    Args:
        VisIt (Any): VisIt module
        setting (Any): setting of the output

    Returns:
        None
    """
    # SaveWindowAttributes object for save file.
    save_window = VisIt.SaveWindowAttributes()

    # loading the user settings.
    save_window.format = save_window.PNG
    save_window.fileName = os.path.join(
        setting.OUTPUT_FILE_PATH,
        r"%s" % (setting.OUTPUT_FILE_NAME))
    save_window.width = setting.FIGURE_WIDTH
    save_window.height = setting.FIGURE_HEIGHT
    save_window.screenCapture = 0

    VisIt.SetSaveWindowAttributes(save_window)

    return


def save_snapshot(VisIt, setting):
    """Save the plotting windows

    Args:
        VisIt (Any): VisIt module
        setting (Any): setting of the output

    Returns:
        None
    """
    save_setting(VisIt, setting)
    save_file_name = VisIt.SaveWindow()
    print(r"%s saved." % (save_file_name))

def save_time_evolve(VisIt, setting):
    """Save the plotting windows

    Args:
        VisIt (Any): VisIt module
        setting (Any): setting of the output

    Returns:
        None
    """
    save_setting(VisIt, setting)
    
    save_file_names = []

    for state in range(VisIt.TimeSliderGetNStates()):
        print(state)
        VisIt.SetTimeSliderState(state)
        save_file_name = VisIt.SaveWindow()
        save_file_names += [save_file_name]
        print(r"%s saved." % (save_file_names[-1]))