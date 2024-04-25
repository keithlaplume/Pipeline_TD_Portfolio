"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""

import getpass
import re
import math
import os
import tempfile
import sys
sys.path.append("█████████████████")
import sb_libs.latest.Deadline.DeadlineConnect as connect
import subprocess

## make sure to use local server to get correct pools and groups
sys.path.append("█████████████████/███████/main/Lib/site-packages")
import ████████

public_ip = ████████.get('https://www.wikipedia.org').headers['X-Client-IP']
if public_ip.startswith(('33', '31')):
    location = '███'
else:
    location = '███'

deadline_server = "████████████" if location == '███' else "████████"


class deadline_submitter(object):
    @staticmethod
    def init_Deadline():
        connectionObject = connect.DeadlineCon(deadline_server, 8082)
        pools = connectionObject.Pools.GetPoolNames()
        groups = connectionObject.Groups.GetGroupNames()
        deadlineCon = {'pools': pools, 'groups': groups}
        return deadlineCon

    @staticmethod
    def populate_nuke_plugininfo_data(nuke_script):
        default_root = "P:/{}".format(os.environ.get('PROJECT_CODE', 'generic'))
        project_path = os.environ.get("PROJECT_ROOT", default_root)

        #create nuke plugin file
        plgInfo = {
            "SceneFile": nuke_script,
            "Version": 11.3,
            "Threads": 0,
            "RamUse": 0,
            "NukeX": False,
            "BatchMode": True,
            "BatchModeIsMovie": False,
            "ContinueOnError": False,
            "RenderMode": "Use Scene Settings",
            "EnforceRenderOrder": False,
            "Views": "",
██████████████████████████████
████████████████████████████
█████████████████████████████
██████████████████████████████
██████████████████████████████████████████
██████████████████████████████████████████
            "ScriptJob": False,
            "ScriptFilename": ""
        }

        return plgInfo

    @staticmethod
    def populate_nuke_jobinfo_data(nuke_script, start_frame, end_frame, frames, fml, priority, batch_name):

        job_name = os.path.basename(nuke_script)
        job_name = job_name.split('.nk')[0]
        job_name = "BTW_{}_comp_render".format(job_name)

        if fml:
            middle_frame = int(math.floor(end_frame / 2))
            render_frames = '{},{},{}'.format(str(start_frame), str(middle_frame), str(end_frame))
        else:
            render_frames = frames

        jobsInfo = {
            "Plugin": "Nuke",
            "Name": job_name,
            "BatchName": batch_name,
            "Comment": "",
            "Department": "Compositing",
            "EnvironmentKeyValue0": "SHOWS_REPO = C:\\██████\\██████████",
            "EnvironmentKeyValue1": "PYTHONPATH = C:\\██████\\███████\\███████\\main\\Lib\\site - packages;C:\\██████\\██████████\\BTW\\nuke\\python;C:\\██████\\███████;C:\\██████\\███████\\pipeline",
            "EnvironmentKeyValue2": "SB_REPO = C:\\██████\\███████",
            "EnvironmentKeyValue3": "FOUNDRY_LICENSE = 37322@sbt-ls1;4101@sbt-ls1",
            "EnvironmentKeyValue4": "PROJECT_CODE = BTW",
            "EnvironmentKeyValue5": "NUKE_PATH = C:\\██████\\██████████\\BTW\\nuke\\plugins\\cryptomatte;C:\\██████\\██████████\\BTW\\nuke\\plugins;C:\\██████\\██████████\\BTW\\nuke\\.nuke;C:\\██████\\███████",
            "Pool": "nuke",
            "SecondaryPool": None,
            "Group": None,
            "Priority": priority,
██████████████████████████████████████
████████████████████████████████████████
██████████████████████████████████
████████████████████████████████████████████████████████
████████████████████████████████████████
            "MachineLimit": 0,
            "Whitelist": "",
            "LimitGroups": "",
            "JobDependencies": "",
            "OnJobComplete": "Nothing",
            "Frames": render_frames,
            "ChunkSize": 1,
            "OverrideTaskFailureDetection": True,
            "FailureDetectionTaskErrors": 3,
            "OverrideJobFailureDetection": True,
            "FailureDetectionJobErrors": 5,
            "UserName": os.getenv('USERNAME')
        }

        return jobsInfo

    @staticmethod
    def populate_encode_plugininfo_data(nuke_script, note):

        nuke_script = os.path.abspath(nuke_script)

        ep = re.search("render\\\(.*)\\\shots", nuke_script).group(1)
        shot = re.search("shots\\\(.*)\\\comp_project", nuke_script).group(1)

        # create nuke plugin file
        plgInfo = {
            "ScriptFile": "C:\\██████\\███████\\libSB\\sb_applications\\sb_deadline\\jobs\\python_wrapper_job\\python_subprocess.py",
            "Arguments": "C:\\██████\\██████████\\BTW\\nuke\\python\\encode_and_upload_comp.py --ep {} --shot {} --note {}".format(ep, shot, note),
            "Version": 2.7,
            "SingleFramesOnly": False
        }

        return plgInfo

    @staticmethod
    def populate_encode_jobinfo_data(nuke_script, job_id, batch_name):
█
██████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████
█
        jobsInfo = {
            "Plugin": "Python_SB",
            "BatchName": batch_name,
            "Comment": "",
            "TaskTimeoutMinutes": 30,
            "LimitGroups": "",
            "Group": "none",
            "Name": job_name,
            "MachineLimit": 0,
            "Whitelist": "",
            "InitialStatus": "Active",
            "EnableAutoTimeout": False,
            "SecondaryPool": "",
            "Priority": 85,
            "LimitConcurrentTasksToNumberOfCpus": True,
            "Department": "",
            "ConcurrentTasks": 1,
            "OnJobComplete": "Nothing",
            "Pool": "nuke",
            "JobDependencies": job_id,
            "Frames": 0,
            "ChunkSize": 1,
            "PreTaskScript": "S:\\sb_deploy\\deployer\\run_deploy_slave.py",
            "EnvironmentKeyValue0": "PROJECT_ROOT = P:\BTW",
            "EnvironmentKeyValue1": "PROJECT_CODE = BTW",
            "EnvironmentKeyValue2": "USERNAME = {}".format(os.getenv('USERNAME')),
            "OverrideTaskFailureDetection": True,
            "FailureDetectionTaskErrors": 1,
            "OverrideJobFailureDetection": True,
            "FailureDetectionJobErrors": 1,
            "UserName": os.getenv('USERNAME')
        }

████████████████████████
█
██████████████████
███████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████
                                                                           frames,
                                                                           fml,
                                                                           priority,
                                                                           batch_name)
        nuke_plugin_info_dict = deadline_submitter.populate_nuke_plugininfo_data(nuke_script)

        # Create deadlinecommand for nuke job file and plugin file
        nuke_job_info_text = ""
        for p in nuke_job_info_dict:
            nuke_job_info_text += "{}={}\n".format(p, nuke_job_info_dict[p])

        nuke_plugin_info_text = ""
        for p in nuke_plugin_info_dict:
            nuke_plugin_info_text += "{}={}\n".format(p, nuke_plugin_info_dict[p])

        nuke_job_info_file = tempfile.mkstemp(suffix="_job_info_{}.txt".format(nuke_job_info_dict["Plugin"]))
        with open(nuke_job_info_file[1], "w") as f:
            f.write(nuke_job_info_text)

        nuke_plugin_info_file = tempfile.mkstemp(suffix="_plugin_info_{}.txt".format(nuke_job_info_dict["Plugin"]))
        with open(nuke_plugin_info_file[1], "w") as f:
            f.write(nuke_plugin_info_text)

        os.close(nuke_job_info_file[0])
        os.close(nuke_plugin_info_file[0])

        # deadline cmd submission command
        ddCommand = "C:\\Progra~1\\Thinkbox\\Deadline10\\bin\\deadlinecommand.exe"
        cmdline = ddCommand + " " + "\"" + nuke_job_info_file[1] + "\"" + " " + "\"" + nuke_plugin_info_file[1]

        process = subprocess.Popen(cmdline, creationflags=subprocess.SW_HIDE, shell=True, stdout=subprocess.PIPE)
        process_result = process.communicate()[0]

█████████████████████████████████████████████████████████████████████
█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████
█
█████████████████████████████████████████████████████████████████████
██████████████████████████████████
███████████████████████████████████████
            encode_job_info_text += "{}={}\n".format(p, encode_job_info_dict[p])

        encode_plugin_info_text = ""
        for p in encode_plugin_info_dict:
            encode_plugin_info_text += "{}={}\n".format(p, encode_plugin_info_dict[p])

        encode_job_info_file = tempfile.mkstemp(suffix="_job_info_{}.txt".format(encode_job_info_dict["Plugin"]))
        with open(encode_job_info_file[1], "w") as f:
            f.write(encode_job_info_text)

        encode_plugin_info_file = tempfile.mkstemp(suffix="_plugin_info_{}.txt".format(encode_job_info_dict["Plugin"]))
        with open(encode_plugin_info_file[1], "w") as f:
            f.write(encode_plugin_info_text)

        os.close(encode_job_info_file[0])
        os.close(encode_plugin_info_file[0])

        # deadline cmd submission command
        ddCommand = "C:\\Progra~1\\Thinkbox\\Deadline10\\bin\\deadlinecommand.exe"
        cmdline = ddCommand + " " + "\"" + encode_job_info_file[1] + "\"" + " " + "\"" + encode_plugin_info_file[1]

        process = subprocess.Popen(cmdline, creationflags=subprocess.SW_HIDE, shell=True, stdout=subprocess.PIPE)
        process_result = process.communicate()[0]

        return True
