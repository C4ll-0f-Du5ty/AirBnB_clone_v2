#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:"""

import os
from fabric.api import put, run, env, local
import datetime

env.hosts = ["54.145.156.142", "54.146.89.30"]


def do_pack():
    """Function to generate a .tgz archive from web_static folder."""
    d = datetime.datetime.utcnow()
    time = f"{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}"
    tarball = f"web_static_{time}.tgz"
    command = f"tar -cvzf versions/{tarball} web_static"

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(command).failed is True:
        return None
    return tarball


def deploy():
    pass
