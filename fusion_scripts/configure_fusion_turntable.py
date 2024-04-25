"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
import os
import sys
import BlackmagicFusion as bmd

if __name__ == '__main__':
    args = sys.argv[1:]
    comp_path = args[0]

    fusion = bmd.scriptapp("Fusion")

    # load comp
    orig_comp = fusion.MapPath(comp_path)
    comp = fusion.LoadComp(orig_comp)

    # get values
    filename = comp.GetAttrs()["COMPS_Name"]
    filepath = comp.GetAttrs()["COMPS_FileName"]
    show_code = filename.split('_')[0]
    asset_name = filename.split('_')[1]
    version = filename.split('v')[1].split('.')[0]
    sb_task = filename.split('_')[2]
    asset_type = filepath.split('\\')[3]
    working_dir = os.path.dirname(os.path.dirname(filepath))
    image_path = os.path.join(working_dir, 'render', '_'.join([show_code, asset_name, sb_task, 'turntable.0001.exr']))
    output_path = os.path.dirname(os.path.dirname(comp_path))
    art_path = os.path.join(os.path.dirname(output_path), "images", "{}_art.PNG".format(sb_task))

    if os.path.isfile(image_path):
        print('Found rendered files')
    else:
        print('Cannot find rendered files')

    #get nodes
    art_node = comp.Art()
    loader_node = comp.Loader1()
    name_node = comp.Name()
    version_node = comp.Version()
    saver_node = comp.Saver1()

    #get client task token
    if sb_task == 'modeling':
        task_token = 'Mo'
    elif sb_task == 'shading':
        task_token = 'Tx'

    #set values
    art_node.Clip = art_path
    loader_node.Clip = image_path
    version_node.SetInput("StyledText", version)
    name_node.SetInput("StyledText", asset_name.upper())
    output_name = os.path.join(output_path, 'output', '_'.join([show_code, asset_name, task_token, 'v' + version + '.mov']))
    saver_node.Clip = output_name

    # save scene
    comp.Save(comp_path)
