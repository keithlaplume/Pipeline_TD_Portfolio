"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
from maya import cmds
import pymel.core as pm

from ██████████████████████ import ███████


def main(camera, start_frame, end_frame, cam_output_file_name):
    camera_shape = cmds.listRelatives(camera, s=True)[0]

    # Create transform null for 2D camera export
    tmp = cmds.spaceLocator(n='RENDER_EXPORT_CAM_2D_data')
    transNull = tmp[0]
    cmds.connectAttr(camera_shape + '.filmTranslateH', transNull + '.translateX')
    cmds.connectAttr(camera_shape + '.filmTranslateV', transNull + '.translateY')
    cmds.connectAttr(camera_shape + '.zoom', transNull + '.scaleX')
    cmds.connectAttr(camera_shape + '.filmRollValue', transNull + '.rotateZ')
    cmds.bakeResults(transNull, t=(float(start_frame) - 1.0, float(end_frame) + 1.0))

    transform_data_file_name = cam_output_file_name.split(".abc")[0] + "_2d_data.abc"

    jobs = []

    transform_data = {
        "root": pm.PyNode(transNull),
        "exportPath": transform_data_file_name,
        "selection": []
    }

    jobs.append(transform_data)

    payload = {
        "verbose": True,
        "userAttrPrefix": "c_",
        "start": start_frame,
        "end": end_frame,
        "jobs": jobs
    }

    abcFiles = ███████.█████████████.█████████(**payload)

    return abcFiles