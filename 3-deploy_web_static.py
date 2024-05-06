#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy:"""

import os
from fabric.api import put, run, env, local
import datetime

env.hosts = ["54.145.156.142", "54.146.89.30"]


def do_pack():
    """Function to generate a .tgz archive from web_static folder."""
    d = datetime.datetime.utcnow()
    time = f"{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}"
    tarball = f"versions/web_static_{time}.tgz"
    command = f"tar -cvzf {tarball} web_static"

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(command).failed is True:
        return None
    return tarball


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False

    file_n = archive_path.split("/")[-1]
    no_ext = file_n.split(".")[0]
    try:
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("rm -rf /data/web_static/releases/{}/".format(no_ext))
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm -rf /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except ValueError:
        return False


def deploy():
    """Automate the Whole Process"""
    Name = do_pack()
    if Name is None:
        return False
    return do_deploy(Name)
