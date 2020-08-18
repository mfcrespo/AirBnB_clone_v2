#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Write a Fabric script that generates a .tgz
    archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack
    """
    datefile = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(datefile))
        return "versions/web_static_{}.tgz".format(datefile)
    except:
        return None
