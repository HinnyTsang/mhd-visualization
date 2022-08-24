"""
    Controlling the camera angle
"""

from default_track import rotation


def set_view(view):
    """
        set viewing angle
    """
    view.viewNormal = (-0.571619, 0.405393, 0.713378)
    view.viewUp = (0.308049, 0.911853, -0.271346)

    return

def set_animate(vst, options = None):
    """
        
    """

    if options == None:
        rotation.set_camera(vst)



if __name__ == "__main__":
    pass