"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
"""This script sets up the selected camera with the correct lens shift"""
render_cam = comp.ActiveTool

if render_cam:
    print('Found Camera')
    render_cam.LensShiftX.SetExpression(
        "-(RENDER_EXPORT_CAM_2D_data.Transform3DOp.Translate.X/2)")
    render_cam.LensShiftY.SetExpression(
        "-(RENDER_EXPORT_CAM_2D_data.Transform3DOp.Translate.Y*ApertureW/ApertureH)/2")
else:
    print('Cannot find Camera named RENDER')
