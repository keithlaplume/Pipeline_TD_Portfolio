"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
import json
import maya.app.renderSetup.model.renderSetup as renderSetup
from maya import cmds
import os

set_exception_list = ["███████████████████████████████████████████"]

def import_light_rig(file_path):
    if os.path.isfile(file_path):
        cmds.file(file_path, i=True)
        print("Light Rig Imported from {}".format(file_path))
        return True
    else:
        print("ERROR: No file found. {} not imported".format(file_path))
        return False


def import_light_sets(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            light_sets_dict = json.load(f)
        for light_set in light_sets_dict:
            for light in light_sets_dict[light_set]:
                cmds.sets(light, include=light_set)
        print("Light Sets Imported from {}".format(file_path))
        return True
    else:
        print("ERROR: No file found. {} not imported".format(file_path))
        return False


def build_vrayop_relationships_from_file(file_path, assets_to_sort):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            vrayop_dict = json.load(file)

        for vrayop in vrayop_dict:
            if vrayop_dict[vrayop]:
                for asset in vrayop_dict[vrayop]:
                    if (cmds.ls(asset)):
                        if asset in assets_to_sort:
                            assets_to_sort.remove(asset)
                            cmds.sets(asset, include=vrayop)
        print("Vray OP relationships read from {}".format(file_path))
        return assets_to_sort
    else:
        print("ERROR: No file found. {} not read".format(file_path))
        return assets_to_sort

def auto_sort_vrayop(assets_to_sort):
█████████████████████████████████
█████████████████████████████████████████████████████████████████████████
████████████████████████████████████████
████████████████████████████████████████████████████
█████████████████████████████████████████
██████████████
            if len(cmds.ls("VRay_OP_set")):
                if "set_" in asset:
                    cmds.sets(asset, include="VRay_OP_set")
                    assets_to_sort.remove(asset)
            if len(cmds.ls("VRay_OP_chr")):
                if "chr_" in asset:
                    cmds.sets(asset, include="VRay_OP_chr")
                    assets_to_sort.remove(asset)
                elif "prp_" in asset:
                    cmds.sets(asset, include="VRay_OP_chr")
                    assets_to_sort.remove(asset)
    return assets_to_sort



def import_render_setup(file_path):
    # delete rogue light editor nodes
    selection = cmds.ls('*lightEditor*')
    if selection:
        print('DELETING:')
        print(selection)
        cmds.delete(selection)
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            renderSetup.instance().decode(json.load(f), renderSetup.DECODE_AND_OVERWRITE, None)
        return True
    else:
        print("ERROR: No file found. {} not imported".format(file_path))
        return False
