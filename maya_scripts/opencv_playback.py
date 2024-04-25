"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
import maya.cmds as cmds
import maya.OpenMaya as om
import cv2
from ██████████████████████████████ import ███████████████
import os
from ███████████████████████████████ import █████████████
from ██████████████████ import ███████████████████████████████
from █████████████████ import ██████████████

global cap
global animatic_paths


def show_frame(type):
    global cap
    global animatic_paths
    current_shot = cmds.sequenceManager(q=True, currentShot=True)
    if current_shot:
        if type == 'anim':
            animatic_path = animatic_paths[current_shot]
            start_frame = cmds.shot(current_shot, q=True, sst=True)
        else:
            animatic_path = animatic_paths['single']
            start_frame = int(cmds.playbackOptions(q=True, animationStartTime=True))

    else:
        try:
            animatic_path = animatic_paths['single']
        except:
            pass
        start_frame = int(cmds.playbackOptions(q=True, animationStartTime=True))
    try:
        cap.open(animatic_path)
        frame_number = (cmds.currentTime(q=True)) - start_frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_number))
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)
    except:
        om.MGlobal.displayError("Unable to find shot at this frame in Sequence. Scrub to nearest shot.")


def run(type):
    # load animatics paths for every shot in the sequence
    project = os.environ.get('PROJECT_CODE')
    shot_data = ███████████████(project).parse_path_from_filename(
        ███████████████.current_open_file())

    if shot_data['shot']:
        shots = cmds.sequenceManager(lsh=True)
        global animatic_paths
████████████████████████████
██████████████████
████████████████████████████████████
████████████████████████████████████████████████████████████
███████████████████████████████████
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████
                                                 shot_name_clean, 'animatic',
                                                 shot_data['ep'] + '_' + shot_name_clean + '.mov').replace('\\', '/')
                    animatic_paths[shot_name] = animatic_path
                else:
                    animatic_path = os.path.join(shot_data['root'], shot_data['branch'], shot_data['ep'], 'sequences',
                                                 shot_data['shot'], 'layout', 'playblasts').replace('\\', '/')
                    newest_playblast = os.listdir(animatic_path)
                    newest_playblast = newest_playblast[(len(newest_playblast) - 1)]
                    animatic_paths['single'] = os.path.join(animatic_path, newest_playblast).replace('\\', '/')
        else:
            if type == 'anim':
                animatic_path = os.path.join(shot_data['root'], shot_data['branch'], shot_data['ep'], 'shots',
                                             shot_data['shot'],
                                             'animatic', shot_data['ep'] + '_' + shot_data['shot'] + '.mov').replace(
                    '\\', '/')
                animatic_paths['single'] = animatic_path
            else:
                task = ██████████████().get_project(project).get_subproject(shot_data['ep'])['aspects'][
                    'project'].get_shot(shot_data['shot']).get_task('layout')
                dest = os.path.join(task['playblast_repository']['path'], task.get_new_playblast_name())
                ███████████████████████████████(destination=dest, task=task)
                animatic_paths['single'] = dest

        global cap
        cap = cv2.VideoCapture()
        cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame', 640, 360)
        cv2.setWindowProperty('Frame', cv2.WND_PROP_TOPMOST, 1)
        if type == 'anim':
            exp = 'python("from mgc.internal.layout.opencv_playback import show_frame;show_frame(\'anim\')")'
        else:
            exp = 'python("from mgc.internal.layout.opencv_playback import show_frame;show_frame(\'pb\')")'

█████████████████████████████████████████████████
███████████████████████
██████████████████████
████████████████████████████████
█████████████████████████████████████
█████████████████████████████████████████
██████████
███████████████████████████
            msg = 'Animatic Could Not Be Loaded'
        else:
            msg = 'Playblast Could Not Be Loaded'

        cmds.confirmDialog(title='Warning', message=msg)


def pre(payload):
    print('*************************')
    print('Closing Open CV Playback')
    cv2.destroyAllWindows()
    print('*************************')


█████████████.sig_load_pre.connect(pre)