import csv
import random

# Возвращает словарь, содержащий 'answer'- ответ и 'countries' все страны раунда
def CreateGame(number_of_countries):
    with open('countries.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        countries = list(reader)
        countries.pop(0)
        print(countries)

        game = dict()
        answer = random.choice(countries)
        game['answer'] = answer
        game_countries = [answer]
        while len(game_countries) != number_of_countries:
            country = random.choice(countries)
            if country[1] != answer[1] and country not in game_countries:
                game_countries.append(country)
        random.shuffle(game_countries)
        game['countries'] = game_countries
        return game

