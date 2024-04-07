#!/usr/bin/python3
"""Write a Fabric script that distributes an archive to your web servers,
using the function do_deploy"""

import os
from fabric.api import put, run, env


def do_deploy(archive_path):
    """UnCompressing an Archive on the webserver"""
    env.hosts = ["100.25.37.19", "54.237.57.128"]

    if os.path.exists(archive_path) is False:
        return False

    try:
        fileName = archive_path.split("/")[-1]
        uncompressedName = fileName.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run(f"mkdir -p {path}{uncompressedName}")
        run(f"tar -xvf /tmp/{fileName} -C {path}{uncompressedName}")
        run(f"rm /tmp/{fileName}")
        run(f"mv {path}{uncompressedName}/web_static/* "
            "{path}{uncompressedName}/")
        run(f"rm -rf {path}{uncompressedName}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path}{uncompressedName}/ /data/web_static/current")
        return True
    except ValueError:
        return False
