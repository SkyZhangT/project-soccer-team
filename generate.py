import json
from faker import Faker
import random
from random import randint
fake = Faker('en_US')

nationality = ['Argentina', 'Belgium', 'Brazil', 'England', 'Spain']
leagues = ['ANKARA', 'Premier League', 'La Liga', 'Serie A', 'Ligue 1']
teams = {'ANKARA': ['Gençlerbirliği', 'Ankara Demirspor', 'Ankaragücü', 'Muhafızgücü', 'Harp Okulu'],
         'Premier League': ['Arsenal', 'Aston Villa', 'Barnsley', 'Birmingham City', 'Blackburn Rovers'],
         'La Liga': ['Real Madrid', 'Barcelona', 'Atlético Madrid', 'Athletic Bilbao', 'Valencia'],
         'Serie A': ['Atalanta', 'Benevento', 'Bologna', 'Cagliari', 'Crotone'],
         'Ligue 1': ['Angers', 'Bordeaux', 'Brest', 'Dijon', 'Lens']}
position = ['GK', 'CB', 'CM', 'RM', 'LM', 'LW', 'RW', 'ST']

player_list = {}

for i in range(100):
    name = fake.unique.name()
    player_list[name] = {}
    player_list[name]['na'] = nationality[randint(0, 4)]
    player_list[name]['league'] = leagues[randint(0, 4)]
    player_list[name]['team'] = teams[player_list[name]
                                      ['league']][randint(0, 4)]
    player_list[name]['rating'] = randint(0, 100)
    player_list[name]['pos'] = position[randint(0, 7)]

fout = open('players.json', 'w')
json.dump(player_list, fout, indent=4)
fout.close()
