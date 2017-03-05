import json
import os
import pathlib
import sys


def load_config():
    config_file = pathlib.Path(
        os.getenv("XDG_CONFIG_HOME", os.getenv("HOME") + "/.config") +
        "/salesforce/credentials")
    if not config_file.is_file():
        print("{} not found".format(config_file))
        sys.exit()
    with config_file.open() as f:
        config = json.load(f)
    return config


if __name__ == "__main__":
    config = load_config()
