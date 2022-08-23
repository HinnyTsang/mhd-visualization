"""
    Setting for volume plot
"""


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

    n_points = 10

    # create gaussian control points
    gaussian_control_points = [vst.GaussianControlPoint() for _ in range(n_points)]

    # setting control points attributes.
    for i, gaussian_control_point in enumerate(gaussian_control_points):
        # width of the distribution
        gaussian_control_point.SetWidth(0.005)
        # x position of the opacity: [0, 1]
        gaussian_control_point.SetX(float(i) / n_points)
        # opacity value at the peak of the distribution: [0, 1]
        gaussian_control_point.SetHeight(float(i) / n_points)

        # Add the control point to the control points list.
        opacity_control_points.AddControlPoints(gaussian_control_point)

    volume_attr.SetOpacityControlPoints(opacity_control_points)

    opacity_control_points = volume_attr.GetOpacityControlPoints()

    vst.SetPlotOptions(volume_attr)
    
    print opacity_control_points.GetNumControlPoints()


    print "Options for OpacityControlPoints: " , dir(opacity_control_points)