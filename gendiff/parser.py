import json

import yaml


def file_parser(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        if '.json' in filepath:
            data_file = json.load(file)
        if '.yaml' in filepath or '.yml' in filepath:
            data_file = yaml.safe_load(file)
    return data_file