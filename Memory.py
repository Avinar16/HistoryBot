import csv
import copy


def Register(tg_id, tg_name):
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)

        InTopFile = False
        for element in config:
            if element['tg_id'] == tg_id:
                print('Was here')
                InTopFile = True
                break
        if not InTopFile:
            config.append({'tg_id': tg_id, 'tg_name': tg_name, 'score': 1, 'current answer': '', 'current game': 0,
                           'current score': 0})
            print('new guy')
        Write(config)


def Write(config):
    with open('top.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=config[0].keys())
        writer.writeheader()
        writer.writerows(config)


def CurrentGame(tg_id, reset=False, add=False):
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)
        number = 0
        for element in config:
            if element['tg_id'] == tg_id:
                if add:
                    element['current game'] = int(element['current game']) + 1
                    number = int(element['current game'])
                    Write(config)
                    return number
                elif reset:
                    element['current score'] = 0
                    element['current game'] = 0
                    element['current answer'] = 0
                    Write(config)
                    return 0
                else:
                    return element['current game']


def GetAnswer(tg_id):
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)

        for element in config:
            if element['tg_id'] == tg_id:
                return element['current answer']


def SetAnswer(tg_id, answer):
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)

        for element in config:
            if element['tg_id'] == tg_id:
                element['current answer'] = answer
        Write(config)


def GetCurrentScore(tg_id):
    with open('top.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        config = list(reader)
        for element in config:
            if element['tg_id'] == tg_id:
                return element['current score']