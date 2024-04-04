#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack."""

from fabric.api import local
import datetime
import os


def do_pack():
    """Function to generate a .tgz archive from web_static folder."""
    now = datetime.datetime.now()
    time = now.strftime("%Y%M%D%H%M%S")
    tarball = f"versions/web_static_{time}.tgz"
    command = f"tr -czf {tarball} web_static"
    local(command)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(command).failed is True:
        return None
    return tarball
