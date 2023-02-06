# code for player classes

# player configs
ACCEPTED_RACES = ['Cat', 'Dog', 'Mouse']

class Hero (): 
    """Player Class."""

    def __init__(self, player_name:str, player_race:str) -> None:
        """
        Create a player. 
        
        Parameters
        ----------
        player_name : str
            User name for hero
        player_race : str
            Choose between Cat, Dog, or Mouse
        
        """
        # check user input
        self._check_player_race(player_race)

        self.player_name = player_name
        self.player_race = player_race
    
    def print_player_details(self): 
        print(f'Player Name: {self.player_name}')
        print(f'\tRace: {self.player_race}')
    
    def _check_player_race(self, player_race:str): 
        if player_race not in ACCEPTED_RACES: 
            raise ValueError(
                f'Please use only accepted player races. f{ACCEPTED_RACES}'
            )