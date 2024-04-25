"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
"""Exports the current light rig from the scene, cleans up the workspace,
recreates the Maya shot, then re-import the old light rig. """
import datetime
import os
import sys
from pprint import pprint
import logging
from █████ import ████████
sys.path.append(r'███████████████████████████████████')
sys.path.append(r'███████████████████████████████████venv/Lib/site-packages')
from █████████ import ███████████████████████████ as ██████████████████
from █████████████████████ import ███
from ████████████ import █████████

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info('-------------------- ███IRONMENT START --------------------')
    pprint(dict(os.environ))
    logger.info('-------------------- ███IRONMENT START --------------------')

    shot = os.getenv('SB_SCOPE')
    task_name = os.getenv('SB_TASK_NAME')
    api = os.getenv('██████')
    user = os.getenv('SB_USER')
    show_name = os.getenv('SB_SHOW')

    logger.info("\n\nProcessing shot: {}".format(shot))

    # get task id
    r = ████████.get('http://sbs-█████.com:9090/api/v1' + '/shots',
                     {'show': show_name, 'name': shot, 'fields': ['shots', 'tasks']})

    tasks = r.json()[0]['tasks']

    for task in tasks:
        if task['name'] == 'Lighting':
            os.environ['SB_TASK_ID'] = str(task['id'])
    #http: // sbs - █████.com: 9090 / api / v1 / shots?project = nmr & show = nm01 & name = 114_0040
    # http://sbs-█████.com:9090/api/v1/paths?project=smash&show=sm01&task-name=lighting&scope=117_0240
    # Use working_file_path_maya  to get maya scenes dir, workspace root check if farm_submissions exists under it

    params = {
        'project': os.getenv('SB_PROJECT'),
        'show': os.getenv('SB_SHOW'),
        'task-name': task_name,
        'scope': shot
    }

    r = ████████.get(api + '/paths', params=params, allow_redirects=True)
█████████████████████████████████
█
█████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████
██████████
█████████████████████████████
        workspace_root = shot_data['working_file_path_maya']

    if os.path.exists(workspace_root):
        latest_maya_wip_file = max([wip for wip in os.listdir(workspace_root) if wip.endswith('.ma')])
        latest_wip_fullpath = os.path.join(workspace_root, latest_maya_wip_file)
    else:
        logger.error("No maya files found!")
        sys.exit(1)

    os.environ['SB_LATEST_WIP_PATH'] = latest_wip_fullpath
    os.environ['SB_WORKSPACE'] = workspace_root
    os.environ['SB_MAYA_LIGHT_IMPORT'] = '1'

    # export light rig
    HERE = os.path.dirname(os.path.abspath(__file__))
    with ███('maya', '2020'):
        script = os.path.join(HERE, 'utils', 'export_lights.py')
        print(os.path.isfile(script))
        print(script)

        for output in █████████(['mayapy', script]):
            print(output, end="")

    # clean lighting workspace
    old_folder = 'old_' + str(datetime.datetime.now()).replace(':', '.')
    path = os.path.join(workspace_root, old_folder)

    os.mkdir(path)

    for filename in os.listdir(workspace_root):
        if filename.endswith(".comp") or filename.endswith(".ma") or filename.endswith(".json"):
            os.rename(os.path.join(workspace_root, filename), os.path.join(path, filename))
█
██████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████
█
█████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████

    os.environ['SB_LATEST_WIP_PATH'] = os.path.join(shot_data['working_shot_file_path_maya'],
                                                    shot + '_lighting_v001.ma')

    os.environ['SB_LIGHT_RIG_PATH'] = light_rig_file_path
    os.environ['SB_MAYA_LIGHT_IMPORT'] = '0'

    with ███('maya', '2020'):
        script = os.path.join(HERE, 'utils', 'import_lights.py')
        print(os.path.isfile(script))
        print(script)

        for output in █████████(['mayapy', script]):
            print(output, end="")

