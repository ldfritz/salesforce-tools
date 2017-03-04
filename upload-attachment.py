from simple_salesforce import Salesforce
import base64
import getopt
import json
import os
import pathlib
import pprint
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
    if len(args) != 2:
        print("error: incorrect number of arguments")
        print(help_message)
        sys.exit()
    if not pathlib.Path(args[1]).is_file():
        print("error: {} not found".format(args[1]))
        print(help_message)
        sys.exit()

    result["parent_id"] = args[0]
    result["filename"] = args[1]
    return result


def upload_attachment(sf, parent_id, filename):
    with open(filename, "rb") as f:
        body = base64.b64encode(f.read()).decode("utf-8")

    return sf.Attachment.create({
        "ParentId": parent_id,
        "Name": filename,
        "body": body
    })


if __name__ == "__main__":
    args = parse_options(sys.argv[1:])
    config = load_config()

    sf = Salesforce(
        username=config["username"],
        password=config["password"],
        security_token=config["security_token"])

    pprint.pprint(upload_attachment(sf, args["parent_id"], args["filename"]))
