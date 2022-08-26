# -*- coding: utf-8 -*-
"""
    Setting for streamline plot
"""

def set_stream_plot(VisIt, volume_attr): 
    """
       
    """

    # FreeformMode, GaussianMode, ColorTableMode
    volume_attr.SetOpacityMode(1)

    # opacity_var_max = volume_attr.GetOpacityVarMax()
    # opacity_var_min = volume_attr.GetOpacityVarMin()

    opacity_control_points = volume_attr.GetOpacityControlPoints()

    # scalar field setting, default, linear
    n_points = 10

    # create gaussian control points
    gaussian_control_points = [VisIt.GaussianControlPoint() for _ in range(n_points)]

    # setting control points attributes.
    for i, gaussian_control_point in enumerate(gaussian_control_points):

        gaussian_control_point.SetWidth(0.01) # width of the distribution 
        gaussian_control_point.SetX(min([float(i) / n_points, 1])) # x position of the opacity: [0, 1]
        gaussian_control_point.SetHeight(min([float(i) / n_points * 3, 1])) # opacity value at the peak of the distribution: [0, 1]


    # Add the control point to the control points list.
    for gaussian_control_point in gaussian_control_points:        
        opacity_control_points.AddControlPoints(gaussian_control_point)

    # update the control points to the volume plot.
    volume_attr.SetOpacityControlPoints(opacity_control_points)

    # update the plot options to VisIt
    VisIt.SetPlotOptions(volume_attr)

if __name__ == "__main__":
    pass