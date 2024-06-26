#!/usr/bin/python3
"""Write a Fabric script that distributes an archive to your web servers,
using the function do_deploy"""

import os
from fabric.api import put, run, env

env.hosts = ["54.145.156.142", "54.146.89.30"]


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
