# -*- coding: utf-8 -*-
"""
    Setting for volume plot
"""

def linear(n_points, x):
    """
        TODO set linear opacity value
    """
    pass

def sigmoid(n_points, x, scale):
    """
        TODO set sigmoid opacity value
    """
    pass

def set_volume_plot(VisIt, field_name): 
    """Initialze the volume plot.

    Args:
        VisIt (Any): VisIt module
        field_name (str): name of the scalar field.

    Returns:
        None
    """

    VisIt.AddPlot("Volume", field_name) # Initialize the plot
    volume_attr = VisIt.VolumeAttributes()
    
    volume_attr.SetOpacityMode(1)
    # Mode of Opacity, 1: FreeformMode, 2: GaussianMode, 3: ColorTableMode.

    opacity_control_points = volume_attr.GetOpacityControlPoints()
    """Control points container of the volume plot."""

    n_points = 10
    """Number of opacity control points, default, linear"""

    gaussian_control_points = [VisIt.GaussianControlPoint() for _ in range(n_points)]
    """create gaussian control points"""

    # setting control points attributes.
    for i, gaussian_control_point in enumerate(gaussian_control_points):

        # STEP 1: width of the distribution 
        gaussian_control_point.SetWidth(0.01)
        # STEP 2: x position of the opacity: [0, 1]
        gaussian_control_point.SetX(min([float(i) / n_points, 1]))
        # STEP 3: opacity value at the peak of the distribution: [0, 1]
        gaussian_control_point.SetHeight(min([float(i) / n_points * 3, 1]))

        # STEP 4: set skewness of the gaussizn
        gaussian_control_point.SetXBias(0)
        gaussian_control_point.SetYBias(0)

    # Add the control point to the control points list.
    for gaussian_control_point in gaussian_control_points:
        opacity_control_points.AddControlPoints(gaussian_control_point)

    # update the control points to the volume plot.
    volume_attr.SetOpacityControlPoints(opacity_control_points)

    # default setting.
    volume_attr.resampleFlag = 1
    volume_attr.resampleTarget = 1000000
    volume_attr.opacityVariable = "default"
    volume_attr.compactVariable = "default"



    # update the plot options to VisIt
    VisIt.SetPlotOptions(volume_attr)

if __name__ == "__main__":
    pass