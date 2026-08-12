# =========================================================
#  utils/config_reader.py
#  Small helper that reads config/config.yaml and returns it
#  as a normal Python dictionary, e.g. config["base_url"]
# =========================================================

import os
import yaml


def get_config():
    # Find the path to config/config.yaml (relative to this file)
    this_folder = os.path.dirname(__file__)
    config_path = os.path.join(this_folder, "..", "config", "config.yaml")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Allow overriding the password from an environment variable
    # instead of writing it in the yaml file (safer).
    # Example (Windows cmd):  set NASENI_PASSWORD=yourpassword
    env_password = os.environ.get("NASENI_PASSWORD")
    if env_password:
        config["login_password"] = env_password

    return config
