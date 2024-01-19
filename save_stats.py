import json
from settings import name_file_stat


def save_stat(name):
    with open(name_file_stat, mode='r') as stat_file:
        data = json.load(stat_file)
    data[name] += 1
    with open(name_file_stat, mode='w') as stat_file:
        json.dump(data, stat_file)
