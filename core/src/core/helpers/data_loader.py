import yaml


def load_yaml_file(path_to_file):
    stream = open(path_to_file, "r")
    docs = yaml.safe_load_all(stream)
    return docs
