from simple_salesforce import Salesforce
import base64
import getopt
import json
import os
import pathlib
import pprint
import requests
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


def parse_options(command_args):
    help_message = """
usage: upload-attachment.py [OPTIONS] ID FILE

Uploads FILE with ID as the ParentId.

Options:
  -h, --help      Display this message and exit.
""".strip()

    result = {}
    opts, args = getopt.gnu_getopt(command_args, "h", ["help"])

    for o, a in opts:
        if o == "-h" or o == "--help":
            print(help_message)
            sys.exit()
    if len(args) != 1:
        print("error: incorrect number of arguments")
        print(help_message)
        sys.exit()

    result["salesforce_id"] = args[0]
    return result


def download_attachment(sf, sf_id):
    doc = sf.Attachment.get(sf_id)
    instance = sf.__dict__["sf_instance"]
    response = requests.get(
        "https://{}{}".format(instance, doc["Body"]),
        headers={"Authorization": "Bearer {}".format(sf.session_id)})

    with open(doc["Name"], "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    args = parse_options(sys.argv[1:])
    config = load_config()

    sf = Salesforce(
        username=config["username"],
        password=config["password"],
        security_token=config["security_token"])

    download_attachment(sf, args["salesforce_id"])
