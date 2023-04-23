from vuja_trail.characters import Player
from vuja_trail.characters import Wagon
import random

class Inventory():
    def __init__(self) -> None:
        # starting inventory
        self.inventory = {
        "food":100,
        "oxen":2,
        "gun" :1,
        "ammo":10,
        "money":100,
        "entertainmentitem": 1
        }

    def show(self): 
        return self.inventory

    def add_new_item(self, item, value): 
        self.inventory[item] = value
    
    def update_add_item(self, item, value): 
        self.inventory[item] = self.inventory[item] + value

    def update_sub_item(self, item, value): 
        self.inventory[item] = self.inventory[item] - value

class WagonTeam(): 

    def __init__(self, player:Player, wagon:Wagon, inventory:Inventory) -> None:
        self.player = player
        self.wagon  = wagon
        self.inventory = inventory


class TrailEvents(): 
    def __init__(self) -> None:
        pass 

    def trigger_event(self, wagon_team:WagonTeam): 
        self.wagon_team = wagon_team

        event_prob = self._get_probablity()

        if event_prob <= 50: 
            self._get_berries() 
        else: 
            print('no events triggered.')

    def _get_probablity(self): 
        event_prob = random.randint(0,100)
        return event_prob
    
    def _get_berries(self): 
        # fine a random amount of berries
        berries = random.randint(1, 20)
        print(f'\nYou found {berries} berries')
        self.wagon_team.inventory.update_add_item('food', berries)
        print(f"\tInventory: \n\t{self.wagon_team.inventory.show()}\n")

class GameProgress(): 
    def __init__(self, wagon_team:WagonTeam) -> None:
        self.wagon_team = wagon_team
        self.events = TrailEvents()

        ## game status ## 
        self.game_condition = True
        self.day = 0
        self.miles = 0 

    def set_game_condition(self, status:bool): 
        self.game_condition = status

    def query_next_move(self): 
        msg = "What would you like to do?\n1) Walk\n2) Rest\n3) Check Status\n4) Exit Game\n"
        user_input = int(input(msg)) 

        if user_input == 1: 
            self._move_forward() 
        elif user_input == 2: 
            self._rest() 
        elif user_input == 3: 
            self._check_status()
        elif user_input == 4: 
            self.exit_game() 

    def _move_forward(self): 
        print("You decided to keep going forward.")
        
        self.events.trigger_event(self.wagon_team)
        
        self.miles = self.miles + 10
        self.day = self.day + 1 
        print(f"You completed {self.miles} miles!")
        
    def _rest(self): 
        print("\nYou decided to rest for a day.")
        self.day = self.day + 1
        print(f"It is now day {self.day}")
    
    def _check_status(self,):
        print(f'Day: {self.day}')
        print(f'Miles Traveled: {self.miles}')
        print('Wagon Team Status:')
        print(f"\tPlayer: {self.wagon_team.player.check_status()}") 
        print(f"\tWagon {self.wagon_team.wagon.check_status()}")
        print(f"Inventory:\n\t{self.wagon_team.inventory.show()}\n")

    
    def exit_game(self):
        self.set_game_condition(False)
        

class TrailProgress(): 
    def __init__(self) -> None:
        self.day = 0 

def run_game(): 

    ## init game ## 
    wagon_team = WagonTeam(
        player=Player(),
        wagon=Wagon(),
        inventory=Inventory(), 
    )
    
    game_progress = GameProgress(wagon_team)


    ## start moves ## 
    while game_progress.game_condition is True:          
        game_progress.query_next_move()
        

if __name__ == '__main__':
    run_game()
