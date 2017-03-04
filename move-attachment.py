from simple_salesforce import Salesforce
import base64
import getpass
import json
import os
import pathlib
import pprint


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
    sf = Salesforce(
        username=config["username"],
        password=config["password"],
        security_token=config["security_token"])

    from_parent_id = "a0B410000037Ja2EAE"
    to_parent_id = "a0B410000037Ja2EAE"

    attachments = sf.query(
        "SELECT Id, Name, Body FROM Attachment WHERE ParentId = '{}'".format(
            from_parent_id))

    pprint.pprint(attachments)
