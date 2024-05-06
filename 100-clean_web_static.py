#!/usr/bin/python3
"""Write a Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean:"""

import os
from fabric.api import run, env, local, lcd, cd

env.hosts = ["54.145.156.142", "54.146.89.30"]


def do_clean(number=0):
    """Removes Out-Dated Files"""
    number = int(number)
    number = 1 if number <= 0 else number
    all_contents = sorted(os.listdir("versions"))
    all = len(all_contents)
    if all <= number:
        pass
    else:
        [all_contents.pop() for i in range(number)]
        with lcd("versions"):
            [local(f"rm {file}") for file in all_contents]
        with cd("/data/web_static/releases"):
            all_contents = [file for file in all_contents
                            if "web_static_" in file]
            [run(f"rm -rf {file}") for file in all_contents]
