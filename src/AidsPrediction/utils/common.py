import os
from box.exceptions import BoxValueError
import yaml
from AidsPrediction.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import pandas as pd
import joblib
import json


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox.
    :param path_to_yaml: path like input
    :raises BoxValueError: if the YAML file is empty
    :return: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates list of directories based on path
    :param path_to_directories: list of path of directories to create
    :ignore_log(bool,optional): ignore if multiple directories are to be created. Defaults to True
    :param verbose:
    :return: None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created successfully: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB
    :param path: path to file
    :return: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"
