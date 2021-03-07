import json
import random
from random import randint
from faker import Faker
import collections
fake = Faker('en_US')

# use data_generator.data() to access data
class data_generator:
    position = ['GK', 'CB', 'CM', 'RM', 'LM', 'LW', 'RW', 'ST']
    teams = {'ANKARA': ['Gençlerbirliği', 'Ankara Demirspor', 'Ankaragücü', 'Muhafızgücü', 'Harp Okulu'],
         'Premier League': ['Arsenal', 'Aston Villa', 'Barnsley', 'Birmingham City', 'Blackburn Rovers'],
         'La Liga': ['Real Madrid', 'Barcelona', 'Atlético Madrid', 'Athletic Bilbao', 'Valencia'],
         'Serie A': ['Atalanta', 'Benevento', 'Bologna', 'Cagliari', 'Crotone'],
         'Ligue 1': ['Angers', 'Bordeaux', 'Brest', 'Dijon', 'Lens']}
    nationality = ['Argentina', 'Belgium', 'Brazil', 'England', 'Spain']
    data = list()
    
    def __init__(self, size: int, nationality: list = None, teams: dict = None, outfile: str = 'players.json'):
        """
        Initialization can takes up to 4 arguments, three of them can be empty and defaulted to the ones above

        args:
        size: an integer size of the dataset desired
        nationality: a list of nations, can be any length
        teams: a dictionaty of league and teams, E.g.: {'league1': [team1, team2, team3]}
        outfile: str, name of the output file
        """
        self.outfile = outfile
        if nationality != None:
            self.nationality = nationality

        if teams != None:
            self.teams = teams

        self.leagues = [key for key in self.teams.keys()]
        self.outfile = outfile
        self.size = size
        self.generate()

    def generate(self) -> list:
        """
        generate can be called by outside function to generate multiple different datasets based on same
        league, team, nation information and distribution
        """
        self.clear_data()
        for i in range(self.size):
            self.data.append(self.generate_one())
        return self.data

    def generate_one(self) -> dict:
        """
        generate can be called by outside function to generate multiple different datasets
        """
        player = collections.defaultdict()
        player['name'] = fake.unique.name()
        player['na'] = self.nationality[randint(0, len(self.nationality)-1)]
        player['league'] = self.leagues[randint(0, len(self.leagues)-1)]
        player['team'] = self.teams[player['league']][randint(0, len(self.teams[player['league']])-1)]
        player['rating'] = randint(0, 100)
        player['pos'] = self.position[randint(0, len(self.position)-1)]
        return player

    def clear_data(self):
        self.data = list()

    def export(self):
        """
        export the generated data to the output file name as a json file.
        """
        with open(self.outfile, 'w') as out:
            json.dump(self.data, out)
        return
        
