"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
import os
import json
import maya.cmds as cmds
import maya.app.renderSetup.model.renderSetup as renderSetup
import logging
from ██████████████████████████████ import ███████████████

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


def break_vray_op():
    print("Breaking VRay OP...")
    # break connections of vray object properties so  they can be exported
    try:
        cmds.select('VRay_*', ne=True)
    except ValueError:
        cmds.warning('No Vray Properties Found. Please check names.')
        cmds.confirmDialog(title='Warning!', message='No Vray Properties Found. Please check names.')
        return False

    vray_groups = dict.fromkeys(cmds.ls(selection=True))
    try:
        cmds.select('lightrig', hi=True)
        light_rig = cmds.ls(selection=True)
    except:
        light_rig = None

    for vray_object in vray_groups:
        vray_children = cmds.sets(vray_object, q=True)
        if vray_children:
            print(vray_children)
            vray_groups[vray_object] = vray_children
            for asset in vray_children:
                if light_rig:
                    if asset not in light_rig:
                        cmds.sets(asset, rm=vray_object)
                else:
                    cmds.sets(asset, rm=vray_object)
    return vray_groups


def rebuild_vrayop(vray_groups):
    print("Rebuild connections...")
    # rebuild vray object properties connections
    if vray_groups:
        for vray_object in vray_groups:
            if vray_groups[vray_object]:
                cmds.sets(vray_groups[vray_object], include=vray_object)
    return True
█
█
██████████████████████████████████████████████████
██████████████████████████████████
██████████████████████████████████████████████████
█████████
        cmds.select('lightrig', hi=True, ne=True)
    except ValueError:
        cmds.warning('No Light Rig Found. Nothing will be exported. Please check light rig name.')
        cmds.confirmDialog(title='Warning!',
                           message='No Light Rig Found. Nothing will be exported. Please check light rig name.')
        return False

    # delete constraints
    for asset in cmds.ls(selection=True):
        if 'parentConstraint' in asset:
            cmds.select(asset)
            cmds.delete()

    cmds.select('lightrig', hi=True, ne=True)

    try:
        cmds.select('VRay_*', ne=True, add=True)
    except ValueError:
        cmds.warning('No Vray Properties Found. None will be exported.')
        cmds.confirmDialog(title='Warning!', message='No Vray Properties Found. None will be exported.')

    print("Exporting Light Rig...")
    cmds.file(light_rig_export_full_path, f=True, exportSelected=True, type="mayaAscii", constraints=False, shader=True)
    print("Light Rig Exported")
    rebuild_vrayop(vray_groups)
    print("Succesfully rebuilt vray groups")
    # reset constraints
    rebuilt_lightgrp_constraints = False
    rebuilt_meshgrp_constraints = False
    lightrig_subgroups = cmds.listRelatives('lightrig', children=True)
    for light_group in lightrig_subgroups:
█████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████████████████
█████████████████
█████████████████████████████████████████████████████████████████████████████████████████
            except:
                print("Problem reconnecting constraints to {}".format(light_group))
            rebuilt_lightgrp_constraints = True
        if "_light_rig_meshes" in light_group:
            print("Found light_rig_meshes group that needs constraint: {}".format(light_group))
            set_name = light_group.split("_light_rig_meshes")[0]
            try:
                cmds.parentConstraint('set_{}:light_rig_meshes'.format(set_name), light_group)
            except:
                print("Problem reconnecting constraints to {}".format(light_group))
            rebuilt_meshgrp_constraints = True
    if not rebuilt_lightgrp_constraints or not rebuilt_meshgrp_constraints:
        cmds.confirmDialog(title='Warning!', message='Error re-connecting light rig constraints.')


def export_renderSetup(filename):
    print("Deleting Light Editor...")
    cmds.select(cl=True)
    cmds.delete(cmds.ls(type='lightEditor'))
    print("Exporting Render Setup...")
    with open(filename, "w+") as file:
        json.dump(renderSetup.instance().encode(None), fp=file, indent=2, sort_keys=True)


def export_light_sets(file_path):
    print("Exporting Light Sets...")
    vray_light_select_sets = cmds.ls('VRay*', type='VRayRenderElementSet')
    light_sets_dict = {}
    for light_set in vray_light_select_sets:
        light_sets_dict[light_set] = cmds.sets(light_set, q=True)

    with open(file_path, "w+") as file:
        json.dump(light_sets_dict, fp=file, indent=2, sort_keys=True)


def export_vrayop(light_vrayop_export_name_full_path):
██████████████████████████████████
██████████████████████████████████
█████████████████████████████████████████████████
████████████████████████████████████████████████████████████████
█████████████████████████████████████
████████████████████████████████
█

def main():
    # check to make sure the vray scene settings render nodes are in the scene
    defaultRendererNodes = renderSetup.instance().encode(None)['sceneSettings']['vray']['defaultRendererNodes']
    if not defaultRendererNodes:
        cmds.warning('No Vray Scene Settings Found. Nothing will be exported')
        cmds.confirmDialog(title='Error!', message='No Vray Scene Settings Found. Nothing will be exported')
        return False
    else:
        asset = ███████████████(os.environ.get('PROJECT_CODE')).parse_path_from_filename(███████████████.current_open_file())

        if not asset:
            raise AssertionError('No file is open')

        root = asset['root']
        branch = asset['branch']
        ep = asset['ep']
        shot_name = asset['shot']
        task = asset['task']

        light_rig_export_path = os.path.join(root, branch, ep, 'shots', shot_name, task, 'render_setup')
        light_rig_export_name = shot_name + "_lighting_light_rig"
        light_settings_export_name = shot_name + '_lighting_renderSetup.json'
        light_sets_export_name = shot_name + '_lighting_lightSets.json'
        light_vrayop_export_name = shot_name + '_lighting_vrayop.json'
        light_rig_export_full_path = os.path.join(light_rig_export_path, light_rig_export_name)
        light_sets_export_full_path = os.path.join(light_rig_export_path, light_sets_export_name)
        light_settings_export_full_path = os.path.join(light_rig_export_path, light_settings_export_name)
        light_vrayop_export_name_full_path = os.path.join(light_rig_export_path, light_vrayop_export_name)
        print(light_settings_export_full_path)
        print(light_sets_export_full_path)

        # Creates the export folder path if it does not exist
        if not os.path.exists(light_rig_export_path):
            os.makedirs(light_rig_export_path)

█████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████
█
        # Grabs all the lights for all vray light select sets
        export_light_sets(light_sets_export_full_path)

        # split vray op and export, reconnect vray op
        export_vrayop(light_vrayop_export_name_full_path)

        # export light rig
        export_light_rig(light_rig_export_full_path)

        cmds.confirmDialog(title='Success!', message='Light Rig and Render Setup Exported')
        return True
