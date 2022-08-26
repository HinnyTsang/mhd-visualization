# -*- coding: utf-8 -*-
"""
    Controlling the camera angle
"""

from default_track import rotation


def set_view(
    VisIt,
    view_normal = (-0.571619, 0.405393, 0.713378),
    view_up = (0.308049, 0.911853, -0.271346)):
    """Set camera from given view normal and direction.

    Args:
        VisIt (Any): VisIt module
        view_normal (Tuple[number]): view normal
        view_up (Tuple[number]): view normal

    Returns:
        None
    """

    view3d = VisIt.GetView3D()
    view3d.viewNormal = view_normal
    view3d.viewUp = view_up
    VisIt.SetView3D(view3d)

    return

def set_animate(VisIt, options = None):
    """
        
    """

    if options == None:
        rotation.set_camera(VisIt)



if __name__ == "__main__":
    pass