#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ["54.145.156.142", "54.146.89.30"]


def do_deploy(archive_path):
    """Uncompressing an achieve"""
    if(not os.exists(archive_path)):
        return False

    path = "/data/web_static/releases/"
    archiveName = archive_path.split("/")[-1]
    fileName = archiveName.split('.')[0]
    put(archive_path, "/tmp/")
    run(f"mkdir -p {path}{fileName}")
    run(f"tar -xfv /tmp/{archiveName} -C {path}{fileName}")
    run(f"rm -rf /tmp/{archive_path}")
