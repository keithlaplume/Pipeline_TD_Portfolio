"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
from maya import cmds
import os
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def main():
    camera_name = "cams_{}_main".format(os.getenv('SB_PROJECT'))

    cmds.select('{}:shake_ctl.translateX'.format(camera_name))
    shake_x = cmds.listConnections(t='animCurve')
    if shake_x:
        cmds.delete(shake_x)
        logging.info('Deleted Camera Shake X')
    cmds.select('{}:shake_ctl.translateY'.format(camera_name))
    shake_y = cmds.listConnections(t='animCurve')
    if shake_y:
        cmds.delete(shake_y)
        logging.info('Deleted Camera Shake Y')

    cmds.setAttr('{}:shake_ctl.translateX'.format(camera_name), 0)
    cmds.setAttr('{}:shake_ctl.translateY'.format(camera_name), 0)
    logging.info('Set Camera Shake to Zero')