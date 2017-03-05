from simple_salesforce import Salesforce
import base64
import getopt
import json
import os
import pathlib
import pprint
import requests
import sys



def connect(username, password, security_token):
    return Salesforce(
        username=username, password=password, security_token=security_token)


def download_attachment(sf, sf_id):
    doc = sf.Attachment.get(sf_id)
    instance = sf.__dict__["sf_instance"]
    response = requests.get(
        "https://{}{}".format(instance, doc["Body"]),
        headers={"Authorization": "Bearer {}".format(sf.session_id)})

    with open(doc["Name"], "wb") as f:
        f.write(response.content)


def upload_attachment(sf, parent_id, filename):
    with open(filename, "rb") as f:
        body = base64.b64encode(f.read()).decode("utf-8")

    return sf.Attachment.create({
        "ParentId": parent_id,
        "Name": filename,
        "body": body
    })


def query(sf, query_string):
    return sf.query(query_string)
