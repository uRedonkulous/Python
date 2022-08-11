from pstats import Stats
from re import I
from unicodedata import name


class Pokemon:

    def __init__(self, type:str, name:str, stats:dict) -> None:
        self.type = type
        self.name = name
        self.stats = stats

        @staticmethod
        def validate_stats(stats_given:dict)



bulbasaur = Pokemon(type = ['grass', 'poison'],name='Bulbasaur',stats={'health':45,'attack':10,'defense':10})

print(bulbasaur.stats)