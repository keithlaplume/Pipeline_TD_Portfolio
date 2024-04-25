"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""

import argparse
import os
from █████████████████ import ██████████████


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ep', type=str, required=True)
    parser.add_argument('--shot', type=str, required=True)
    parser.add_argument('--note', type=str, required=True)
    args = parser.██████████()

    project = ██████████████().get_project(os.environ.get('PROJECT_CODE'))
    sb_shot = project.get_subproject(args.ep).get_shot(args.shot)
    result = sb_shot.encode_comp(text="", startframe="0001", note=args.note, prefix="btw_comp_Cp_v01")
