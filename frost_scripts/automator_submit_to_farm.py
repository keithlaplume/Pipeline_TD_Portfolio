"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""

"""This script renders the lighting job.
It finds the latest lighting files and submits it to the farm
If the lighting file doesn't exist, it will be built

DEFAULTS:
FML
all layers from Render layer naming conventions
Set layer single frame only
OPTIONS:
frames=FULL or FML
layers=chr,prp,set,shd,spt,crd,sky,mat,fx,ray,hot,utl,chr_wilbur,
        chr_fg,chr_bg,fx_crd,fx_shd,set_fx,set_spt
extra_layers=
set_full=True or False

Separate multiple options with a space
"""
from subprocess import PIPE, Popen

import os
import sys
from pprint import pprint
import logging
sys.path.append(r'███████████████████████████████████')
from ████████████ import █████████
sys.path.append(r'███████████████████████████████████venv/Lib/site-packages')
from █████████ import ███████████████████████████ as ██████████████████
from █████████████████████ import ███

# sys.path.append(r'N:\Pipeline\software\py█████\release')
from █████ import ████████

logger = logging.getLogger(__name__)

def get_shot_info_with_frames(_api, show, name):
    """Returns a dictionary with shot info

    Args:
        _api: Storm API to use
        show: show code
        name: shot_code (ex: 117_0030)

    Returns: dict containing -
        id, name, type for the shot itself,
        id, name, type for all shot tasks,
        id, name, type for any parent shot,
        id, name, type for any child shots,
        start and end frames for this shot
    """

██████████████████████████████████████
██████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████████████████████████████████
                                                             'code',
                                                             'tasks'
                                                             ]
                      }
                     )

    if r.status_code != 200:
        raise ValueError(r.reason)

    return r.json()[0]

if __name__ == "__main__":
    shot = os.getenv('SB_SCOPE')
    task_name = os.getenv('SB_TASK_NAME')
    api = os.getenv('██████')
    user = os.getenv('SB_USER')
    show_name = os.getenv('SB_SHOW')

    print("\n\nProcessing shot: {}".format(shot))

    # http://sbs-█████.com:9090/api/v1/paths?project=smash&show=sm01&task-name=lighting&scope=117_0240
    # Use working_file_path_maya  to get maya scenes dir, workspace root check if farm_submissions exists under it

    params = {
        'project': os.getenv('SB_PROJECT'),
        'show': os.getenv('SB_SHOW'),
        'task-name': task_name,
        'scope': shot
    }

    r = ████████.get(api + '/paths', params=params, allow_redirects=True)
█
█████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████
██████████
█████████████████████████████
█████████████████████████████████████████████████████████████
█
    shot_info = get_shot_info_with_frames(api, show_name, shot)
    # Get lighting task ID - skip shot if no lighting task found

    task_id = ''
    for task in shot_info['tasks']:
        if task['name'].lower() == 'lighting':
            task_id = str(task['id'])

    if not task_id:
        logger.error("Could not get lighting task id, Skipping shot: {}\n".format(shot))
        sys.exit(1)

    os.environ['SB_TASK_ID'] = task_id

    print('-------------------- ███IRONMENT START --------------------')
    pprint(dict(os.environ))
    print('-------------------- ███IRONMENT START --------------------')

    # create version 1 if file does not exist
    ██████████████████(parent=None, show_code=show_name, api=api, user=user, operation='setup', task='lighting',
                       dcc_name='', dcc_version='')

    if os.path.exists(workspace_root):
        try:
            latest_maya_wip_file = max([wip for wip in os.listdir(workspace_root) if wip.endswith('.ma')])
            latest_wip_fullpath = os.path.join(workspace_root, latest_maya_wip_file)
        except Exception as e:
            logger.error("No maya files found! {}".format(e))
            sys.exit(1)
    else:
        logger.error("No Workspace!")
        sys.exit(1)
█
███████████████████████
█████████████████████████████████████████████
███████████████████████████████████████████████████████████
████████████████████████████████████████████████
██████████████████████████████████████████████████████████████

    HERE = os.path.dirname(os.path.abspath(__file__))
    print('line122')
    with ███('maya', '2020'):
        script = os.path.join(HERE, 'utils', 'maya_lighting_render.py')
        print(os.path.isfile(script))
        print(script)

        for output in █████████(['mayapy', script]):
            print(output, end="")

