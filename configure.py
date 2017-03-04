import os
import pathlib

config_file = pathlib.Path(
    os.getenv("XDG_CONFIG_HOME", os.getenv("HOME") + "/.config") +
    "/salesforce/credentials")

if not config_file.parent.is_dir():
    print("creating {}".format(config_file.parent))
    config_file.parent.mkdir()

if not config_file.is_file():
    print("creating {}".format(config_file))
    config_file.touch()
