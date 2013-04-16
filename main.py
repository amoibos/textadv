import random
import itertools
import os
import platform
import pickle
import game
import sys


# clear display win/linux
def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

#  asks user for input, menu_section is the "input label"
def user_input(menu_section):
    while True:
        try:
            user_data = int(input(menu_section))
            if user_data == "":
                print("Enter a number")
            else:
                return user_data
        except ValueError:
            print("Only numbers")


#run a instance of GameCreate, display "ingame" menu
def run_game(Game):
    while True:

        if Game.state == "over":
            break
        else:
            pass

        print("1 Battle")
        print("2 Character menu")
        print("3 Save Game")
        print("4 Exit Game")

        game_menu = int(user_input("Game menu:"))
        if game_menu == 1:  # start battle
            clear()
            pass
        elif game_menu == 2:  # character menu
            clear()
            Game.character_menu()
            continue
        elif game_menu == 3:  # save game
            try:
                with open("data.pickle", "wb") as f:
                    pickle.dump(Game, f, pickle.HIGHEST_PROTOCOL)
                    print("Game saved successfull")
                    x = input("Hit enter to continue")
                    clear()
            except:
                print("Problem with saving game")  # need to improve this
            continue
        elif Game_menu == 4:
            sys.exit(0)

        while True:  # battle sequence
            Game.info()
            print(Game.player.character_status())
            print(Game.opponent.character_status())
            print("\n")
            
            if Game.battle_sequence() is False:
                break

            x = input("hit enter to continue")
            clear()
    print("Game over: 1")

# main menu, creates or loads a game instance
def main():
    while True:
        clear()
        print("""
            1 New Game
            2 Continue Game
            4 Exit""")

        menu_selection = int(user_input("Main menu:"))

        if menu_selection == 1:
            clear()
            game_session = game.CreateGame()
            run_game(game_session)
        elif menu_selection == 2:
            with open("data.pickle", "rb") as f:
                game_data = pickle.load(f)
            run_game(game_data)
        elif menu_selection == 3:
            print("3...")
        else:
            print("exit ctrl + c")

if __name__ == "__main__":
    main()
