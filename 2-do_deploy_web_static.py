#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime
from os.path import isfile

env.hosts = ['35.243.243.216', '54.146.219.183']


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


def do_deploy(archive_path):
    """
    Write a Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy
    """

    if isfile(archive_path) is False:
        return False

    try:
        archive_path = "versions/web_static_20200818015236.tgz"
        filename = archive_path.split("/")[1]
        filename1 = (archive_path.split("/")[1]).split(".")[0]
        input_path = "/data/web_static/releases/{}/".format(filename1)
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(input_path))
        run("sudo tar -zxvf /tmp/{} -C {}".format(filename, input_path))
        run("sudo rm -rf /tmp/{}".format(filename))
        run("sudo mv -n {}/web_static/* {}".format(input_path, input_path))
        run("sudo rm -rf {}/web_static".format(input_path))
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(input_path))
        return True

    except Exception:
        return False
