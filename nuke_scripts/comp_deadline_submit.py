"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
import logging
import getpass
import nuke
import nukescripts
import os

from █████ import ████████

logger = logging.getLogger(__name__)


def create_nuke_dirs_WriteTank():

    for node in nuke.allNodes():

        if node.Class() == 'WriteTank':
            sequence = os.path.join(
                node.knobs()['path_context'].value(),
                node.knobs()['path_local'].value(),
                node.knobs()['path_filename'].value()
                )
            folder = os.path.dirname(sequence)
            if os.path.exists(folder):
                print ('render directory was already created')
            else:
                os.makedirs(os.path.dirname(sequence))
                print ('render directory directory has been created')


def submit_scene_to_farm():
    '''
        To be triggered from within nuke via button.
    :return:
    '''
    # nuke.scriptSave()
    sb_api = os.getenv('██████', 'http://sbs-█████.com:9090/api/v1')
    nuke_license = os.getenv('FOUNDRY_LICENSE')

    paths = ████████.get(sb_api + '/paths', {'show': os.getenv('SB_SHOW'),
                                             'task-name': os.getenv('SB_TASK_NAME'),
                                             'scope': os.getenv('SB_SCOPE'),
                                             'user': os.getenv('SB_CURRENT_USER')}).json()
    nuke_path = paths.get("nuke_path")
    shot_audio_path = paths.get("audio_file_path")

    name_list = []
    for item in nuke.allNodes('Write'):
        name_list.append(item.name())

████████████████████████████████████████████
██████████████████████████████████████
█
█████████████████████████████████
█
█████████████████████████████████████████████████
    logger.info(name_list)

    if len(name_list) > 1:
        nuke.message('More than 1 Output Node.')
        raise Exception('More than 1 Output Node.')

    if len(name_list) <= 0:
        logger.critical('No Output Node.')
        raise Exception('No Output Node.')

    sb_output_node = name_list[0]
    output_node = nuke.toNode(sb_output_node)
    if output_node.Class() == 'WriteTank':
        output = os.path.join(
                    output_node.knobs()['path_context'].value(),
                    output_node.knobs()['path_local'].value(),
                    output_node.knobs()['path_filename'].value()
                    )
        output = output.replace('%04d', '####')
    elif output_node.Class() == 'Write':
        output = output_node.knob('file').getValue()
        output = output.replace('%04d', '####')

    _filename = nuke.root()['name'].value()
    logger.info('Filename: %s' % _filename)

    _scope = os.getenv("SB_SCOPE")

    _user = getpass.getuser()

    _comment = "Auto Submission - Nuke Render"
█
██████████████████████████████████████████████████████████████████████
█
██████████████████████████████████████████████████████████████████
█
    _write_node = sb_output_node

    _extra_env = ['FOUNDRY_LICENSE={}'.format(nuke_license),
                  'NUKE_PATH={}'.format(nuke_path),
                  'SB_EP_NUM={}'.format(os.getenv('SB_EP_NUM')),
                  'SB_SHOT={}'.format(os.getenv('SB_SHOT'))]  # for relative paths

    start_frame = nuke.root().knob('first_frame').getValue()
    end_frame = nuke.root().knob('last_frame').getValue()

    _pool = 'nuke'
    _group = 'farm'

    _output_file_name = [os.path.split(output)[1]]  # get output files for deadline GUI
    _output_directory = [os.path.split(output)[0]]  # get output dirs for deadline GUI
    _project_path = os.path.split(_filename)[0]  # get project path

    _aux_files = [_filename]  # get auxillary files to send along with job

    class RenderPanel(nukescripts.PythonPanel):
        def __init__(self):
            nukescripts.PythonPanel.__init__(self, 'Submit to Farm')
            self.dnKnob = nuke.Boolean_Knob('denoise_cb', 'Denoise Rendered Frames in NeatVideo?', True)
            self.dnKnob.setFlag(nuke.STARTLINE)
            self.upKnob = nuke.Boolean_Knob('upload_cb', 'Upload Rendered Frames to Shotgun?', True)
            self.upKnob.setFlag(nuke.STARTLINE)
            self.fmlKnob = nuke.Boolean_Knob('fml_cb', 'FML?', False)
            self.fmlKnob.setFlag(nuke.STARTLINE)
            self.spacer = nuke.Text_Knob('')
            self.strKnob = nuke.Multiline_Eval_String_Knob('comment_mes', 'Comment:')
            self.addKnob(self.dnKnob)
            self.addKnob(self.upKnob)
            self.addKnob(self.fmlKnob)
            self.addKnob(self.strKnob)
██████████████████████████████████████
█
█
█████████████████████████████████████
█████████████████████████████████████
                if knob.value():
                    self.dnKnob.setValue(False)
                    self.dnKnob.setFlag(nuke.DISABLED)
                else:
                    # self.dnKnob.setValue(False)
                    self.dnKnob.clearFlag(nuke.DISABLED)

    p = RenderPanel()
    if p.showModalDialog():
        noise_opt = p.dnKnob.value()
        upload_opt = p.upKnob.value()
        fml_opt = p.fmlKnob.value()
        _comment = p.strKnob.value()

        if fml_opt:
            # get FML info from SG?
            mid_frame = start_frame+((end_frame-start_frame)/2)
            _frames = str("%d,%d,%d" % (start_frame, mid_frame, end_frame))
            desc = 'Automated Conversion (FML)'
            _priority = '51'
        else:
            _frames = str("%d-%d" % (start_frame, end_frame))  # get frames
            desc = 'Automated Conversion'
            _priority = '50'

        _utp_a_source = shot_audio_path
        output = output.replace("\\", "/")

        if _output_directory:
            if not os.path.exists(_output_directory[0]):
                os.makedirs(_output_directory[0])

█████████████████████████████████████████████
█████████████████████████████
████████████████████████████████████████████████████████
█
        # Shotgun Information
        _description = desc

        version = os.path.splitext(_name.split("_")[-1])[0]
        job_name = '{}-{}-{}-{}'.format(os.getenv("SB_SHOW"), os.getenv("SB_TASK_NAME"), _scope,
                                        version)

        params = {'api': sb_api,
                  'aux-files': _aux_files,
                  'comment': _comment,
                  'description': _description,
                  'extra-env': _extra_env,
                  'filename': _filename,
                  'frames': _frames,
                  'name': job_name,
                  'output-filename': _output_file_name,
                  'output-directory': _output_directory,
                  'plugin-name': 'fn03-nuke',
                  'plugin-version': '11.3v3',
                  'pools': _pool,
                  'priority': _priority,
                  'project-path': _project_path,
                  'show': 'fn03',
                  'scope': _scope,
                  'task-id': os.getenv("SB_TASK_ID"),
                  'task-name': 'comp',
                  'user': _user,
                  # 'utp-ao': 'True',
                  'utp-start-number': _utp_start_number,
                  'utp-aud': _utp_a_source,
                  'utp-dst': _utp_dest,
                  'utp-src': _utp_source,
                  'write-node': _write_node
████████████████████
█
██████████████████████
█████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████
█
███████████████████████████
            [params.pop(key) for key in ['utp-start-number', 'utp-aud', 'utp-dst', 'utp-src']]

        r = ████████.post('http://sb-docker-01:6060/api/v1/jobs', params=params)
        logger.info(r.json())

        if r.status_code == 200:
            nuke.message('Job Sent to farm: %s\nWith Job ID #:%s' % (_name, r.json()['_id']))
        else:
            nuke.message('Failed to submit job:\n'
                         'Status: {}\n'
                         'Reason: {}'.format(r.status_code, r.text))
