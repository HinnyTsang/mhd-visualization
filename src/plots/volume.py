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

def set_volume_plot(vst, volume_attr): 
    """
        Available setting
        'GetColorControlPoints',
        'GetColorVarMax',
        'GetColorVarMin',
        'GetCompactVariable',
        'GetFreeformOpacity',
        'GetGradientType',
        'GetLegendFlag',
        'GetLightingFlag',
        'GetLimitsMode',
        'GetLowGradientLightingClampFlag',
        'GetLowGradientLightingClampValue',
        'GetLowGradientLightingReduction',
        'GetMaterialProperties',
        'GetOpacityAttenuation',
        'GetOpacityControlPoints',
        'GetOpacityMode',
        'GetOpacityVarMax',
        'GetOpacityVarMin',
        'GetOpacityVariable',
        'GetOsprayAoDistance',
        'GetOsprayAoSamples',
        'GetOsprayAoTransparencyEnabledFlag',
        'GetOsprayMinContribution',
        'GetOsprayOneSidedLightingFlag',
        'GetOsprayPreIntegrationFlag',
        'GetOsprayShadowsEnabledFlag',
        'GetOspraySingleShadeFlag',
        'GetOspraySpp',
        'GetOsprayUseGridAcceleratorFlag',
        'GetRendererSamples',
        'GetRendererType',
        'GetResampleFlag',
        'GetResampleTarget',
        'GetSamplesPerRay',
        'GetSampling',
        'GetScaling',
        'GetSkewFactor',
        'GetSmoothData',
        'GetUseColorVarMax',
        'GetUseColorVarMin',
        'GetUseOpacityVarMax',
        'GetUseOpacityVarMin',
        'Notify',
        'SetColorControlPoints',
        'SetColorVarMax',
        'SetColorVarMin',
        'SetCompactVariable',
        'SetFreeformOpacity',
        'SetGradientType',
        'SetLegendFlag',
        'SetLightingFlag',
        'SetLimitsMode',
        'SetLowGradientLightingClampFlag',
        'SetLowGradientLightingClampValue',
        'SetLowGradientLightingReduction',
        'SetMaterialProperties',
        'SetOpacityAttenuation',
        'SetOpacityControlPoints',
        'SetOpacityMode',
        'SetOpacityVarMax',
        'SetOpacityVarMin',
        'SetOpacityVariable',
        'SetOsprayAoDistance',
        'SetOsprayAoSamples',
        'SetOsprayAoTransparencyEnabledFlag',
        'SetOsprayMinContribution',
        'SetOsprayOneSidedLightingFlag',
        'SetOsprayPreIntegrationFlag',
        'SetOsprayShadowsEnabledFlag',
        'SetOspraySingleShadeFlag',
        'SetOspraySpp',
        'SetOsprayUseGridAcceleratorFlag',
        'SetRendererSamples',
        'SetRendererType',
        'SetResampleFlag',
        'SetResampleTarget',
        'SetSamplesPerRay',
        'SetSampling',
        'SetScaling',
        'SetSkewFactor',
        'SetSmoothData',
        'SetUseColorVarMax',
        'SetUseColorVarMin',
        'SetUseOpacityVarMax',
        'SetUseOpacityVarMin'
    """

    # FreeformMode, GaussianMode, ColorTableMode
    volume_attr.SetOpacityMode(1)

    # opacity_var_max = volume_attr.GetOpacityVarMax()
    # opacity_var_min = volume_attr.GetOpacityVarMin()

    opacity_control_points = volume_attr.GetOpacityControlPoints()

    # scalar field setting, default, linear
    n_points = 10

    # create gaussian control points
    gaussian_control_points = [vst.GaussianControlPoint() for _ in range(n_points)]

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
    vst.SetPlotOptions(volume_attr)

if __name__ == "__main__":
    pass