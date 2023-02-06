# the main running script
from vuja_trail.player import Hero

def create_player(): 
    player_name = input('Name your Hero: ')    
    player_race = input('Choose Dog, Cat, or Mouse hero: ')

    # initalize player class 
    hero = Hero(
        player_name=player_name,
        player_race=player_race
    )
    print('\nGreat, here are your player details...')
    hero.print_player_details()
    return hero


class RunGame(): 
    pass

def main(): 
    print('Hello Vuk!')
    hero = create_player()

if __name__ == '__main__':
    main()
