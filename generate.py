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

player_list = []

for i in range(100):
    player = {}
    player['name'] = fake.name()
    player['na'] = nationality[randint(0, 4)]
    player['league'] = leagues[randint(0, 4)]
    player['team'] = teams[player['league']][randint(0, 4)]
    player['rating'] = randint(0, 100)
    player['pos'] = position[randint(0, 7)]
    player_list.append(player)

fout = open('players.json', 'w')
json.dump(player_list, fout)
fout.close()
