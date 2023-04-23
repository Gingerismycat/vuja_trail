
#%% 
class Player():
    def __init__(self) -> None:
        # starting player stats
        self.health = 100 
        self.stamina = 100
        self.morale = 100 
        self.hunger = 100

    def check_status(self): 
        return self.__dict__


class Wagon(): 
    def __init__(self) -> None:
        self.wagon_health = 100
    
    def check_status(self): 
        return self.__dict__


class Carpenter(): 
    def __init__(self) -> None:
        pass
    # starting Carpenter stats
        self.health = 100 
        self.stamina = 100
        self.morale = 100 
        self.hunger = 100

class Hunter(): 
    ... 

class Missionary(): 
    ... 


class GameStatus(): 
    def __init__(self) -> None:
        self.day = 0 
    

### testing ### 
if __name__ == '__main__':
    foo = Player() 
    foo.check_status() 


    gs = GameStatus() 
    while gs.day < 5: 
        print(gs.day)
        gs.day = gs.day + 1
        


# %%
