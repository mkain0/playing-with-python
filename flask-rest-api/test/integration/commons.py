import json
from os.path import join, dirname


def load_json(filename):
    relative_path = join('resources', filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
