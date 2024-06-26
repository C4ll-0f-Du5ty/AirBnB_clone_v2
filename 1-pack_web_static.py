#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack."""

from fabric.api import local
import datetime
import os


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
