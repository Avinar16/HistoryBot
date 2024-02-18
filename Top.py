import csv
import copy
from Memory import Write


def AddScore(tg_id):
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)

        # InTopFile = False
        for element in config:
            if element['tg_id'] == tg_id:
                element['score'] = int(element['score']) + 1
                element['current score'] = int(element['current score']) + 1
                break
    Write(config)


def GetTop():
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)

        config = sorted(config, key=lambda x: int(x['score']), reverse=True)

        i = 0
        top = []
        for user in config:
            top.append((user['tg_name'], user['score']))
            if i > 5:
                break
            i += 1
        return top