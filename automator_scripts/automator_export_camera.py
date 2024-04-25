"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
"""This exports the camera with the 2D Lens shift"""

import os
import sys
from pprint import pprint
import logging
import maya.cmds as cmds
import maya.standalone as std
import maya.mel as mel

from █████ import ████████


def create_and_attach_camera(camera='', start_frame='', end_frame=''):
    camera_shape = cmds.listRelatives(camera, s=True)[0]

    # Create transform null for 2D camera export
    tmp = cmds.spaceLocator(n='RENDER_EXPORT_CAM_2D_data')
    transNull = tmp[0]
    cmds.connectAttr(camera_shape + '.filmTranslateH', transNull + '.translateX')
    cmds.connectAttr(camera_shape + '.filmTranslateV', transNull + '.translateY')
    cmds.connectAttr(camera_shape + '.zoom', transNull + '.scaleX')
    cmds.connectAttr(camera_shape + '.filmRollValue', transNull + '.rotateZ')
    cmds.bakeResults(transNull, t=(float(start_frame) - 1.0, float(end_frame) + 1.0))

    # duplicate cam
    new_cam = cmds.duplicate(camera)[0]
    new_cam_shape = cmds.listRelatives(new_cam, s=True)[0]

    # make attrs keyable
    cmds.setAttr(new_cam_shape + ".filmTranslateH", k=True)
    cmds.setAttr(new_cam_shape + ".filmTranslateV", k=True)

    # unlock all keyable attrs
    for atr in cmds.listAttr(new_cam, k=True):
        cmds.setAttr((new_cam + '.' + atr), lock=False)
    for atr in cmds.listAttr(new_cam_shape, k=True):
        cmds.setAttr((new_cam_shape + '.' + atr), lock=False)

    # parent to worldspace
    new_cam = cmds.parent(new_cam, w=True)[0]

    # connect all attributes from orig to new
    prnt_cnst = cmds.parentConstraint(camera, new_cam)

    # connect attributes from constraints that are constrained to the camera
    cam_name = mel.eval('rootOf ' + camera)
    cons_list = [x for x in cmds.listRelatives(cam_name, ad=True, type='constraint')]
    if len(cons_list) > 0:
        prnt_cnst_list = cmds.parentConstraint(new_cam_shape, cons_list)
█
█████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████████████
█████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████

    # bake
    cmds.bakeResults(new_cam, s=True, at=(cmds.listAttr(new_cam, k=True) + cmds.listAttr(new_cam_shape, k=True)),
                     t=(float(start_frame), float(end_frame)))

    cmds.delete(prnt_cnst)

    # set Infinity's to linear to continue curves
    cmds.setInfinity(new_cam, preInfinite='linear', postInfinite='linear')

    return new_cam, new_cam_shape


def find_cam():
    _camera = None
    _cams = cmds.ls(type="camera")
    for _cam in _cams:
        if cmds.getAttr(_cam + ".renderable") == 1:
            if _cam.split(":")[-1] == "RENDERShape":
                _camera = _cam
    return mel.eval('rootOf ' + _camera)


def cam_to_abc():
    start_frame = int(cmds.playbackOptions(q=1, minTime=1))
    end_frame = int(cmds.playbackOptions(q=1, maxTime=1))
    scope = os.getenv('SB_SCOPE')
    show = os.getenv('SB_SHOW')
    episode_number = scope.split('_')[0]
    shot_number = scope.split('_')[1]
    api = os.getenv('██████')
    response = ████████.get(
        "{}/paths?show={}&task-name={}&scope={}".format(os.getenv('SB_PATHS_API', api), show,
███████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████
███████████████████████████████████████████████████████████████████
    cmds.select(_cam_name[1:] + ':RENDER')

    new_cam, new_cam_shape = create_and_attach_camera(
        camera=_cam_name[1:] + ':RENDER',
        start_frame=str(start_frame), end_frame=str(end_frame))
    root_node = cmds.group(new_cam, name='root')
    cmds.parent('RENDER_EXPORT_CAM_2D_data', root_node)  # Parent null to the root node
    cmds.AbcExport(j='-frameRange ' + str(start_frame - 1) + ' ' + str(
        end_frame + 1) + ' -stripNamespaces -worldSpace -dataFormat ogawa -root ' + root_node +
                     ' -file ' + abc_full_path)

    # Delete root node after export
    cmds.delete(root_node)

    return abc_folder_path, abc_full_path

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info('-------------------- ███IRONMENT START --------------------')
    pprint(dict(os.environ))
    logger.info('-------------------- ███IRONMENT START --------------------')

    shot = os.getenv('SB_SCOPE')
    task_name = os.getenv('SB_TASK_NAME')
    api = os.getenv('██████')

    logger.info("\n\nProcessing shot: {}".format(shot))

    # http://sbs-█████.com:9090/api/v1/paths?project=smash&show=sm01&task-name=lighting&scope=117_0240
    # Use working_file_path_maya  to get maya scenes dir, workspace root check if farm_submissions exists under it
█
███████████████
████████████████████████████████████████████
██████████████████████████████████████
████████████████████████████████
        'scope': shot
    }

    r = ████████.get(api + '/paths', params=params, allow_redirects=True)
    logger.info('URL: ' + r.url)

    if r.status_code != 200:
        raise Exception('Could not get shot wip paths from Storm API. Skipping shot...')
    else:
        shot_data = r.json()
        workspace_root = shot_data['working_file_path_maya']

    if os.path.exists(workspace_root):
        latest_maya_wip_file = max([wip for wip in os.listdir(workspace_root) if wip.endswith('.ma')])
        latest_wip_fullpath = os.path.join(workspace_root, latest_maya_wip_file)
    else:
        logger.error("No maya files found!")
        sys.exit(1)

    std.initialize()
    cmds.file(latest_wip_fullpath, open=True, force=True)
    cam_to_abc()
    std.uninitialize()