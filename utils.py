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
    league_nation = {'ANKARA': 'Turkey', 
                    'Premier League': 'England',
                    'La Liga': 'Spain',
                    'Serie A': 'Italy',
                    'Ligue 1': 'France'}
    data = list()
    
    def __init__(self, size: int, league_nation: list = None, teams: dict = None, outfile: str = 'players.json'):
        """
        Initialization can takes up to 4 arguments, three of them can be empty and defaulted to the ones above

        args:
        size: an integer of desired size of the dataset
        nationality: a list of nations, can be any length
        teams: a dictionaty of league and teams, E.g.: {'league1': [team1, team2, team3]}
        outfile: str, name of the output file
        """
        self.outfile = outfile
        if league_nation != None:
            self.league_nation = league_nation

        if teams != None:
            self.teams = teams

        self.leagues = [key for key in self.teams.keys()]
        self.nationality = [self.league_nation[key] for key in self.leagues]
        self.outfile = outfile
        self.size = size
        self.generate()

    def generate(self) -> list:
        """
        generate can be called by outside callers to generate multiple different datasets based on same
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
        player['league'] = self.leagues[randint(0, len(self.leagues)-1)]
        player['team'] = self.teams[player['league']][randint(0, len(self.teams[player['league']])-1)]

        if randint(1, 10) <= 5:
            player['na'] = self.league_nation[player['league']]
        else:
            player['na'] = self.nationality[randint(0, len(self.nationality)-1)]

        player['rating'] = randint(70, 100)
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
        
