import random
import itertools
import os
import platform
import pickle
import game
import sys

class Menu(object):
    def __init__(self, mID, mlabel, mtype):
        self.mID = mID  # Number displayed besides "mlabel"
        self.mlabel = mlabel  # for example "New game"
        self.mtype = mtype  # defines the menu category "main", "game"...

    def print_menu_entry(self):
        print("{0} {1}".format(self.mID, self.mlabel))

    def is_main(self):
        return self.mtype == "main"

    def is_battle(self):
        return self.mtype == "battle"

    def command_main(self):
        if self.is_main():
            if self.mID == 1:
                clear()
                run_game(game.CreateGame())
            elif self.mID == 2:
                with open("data.pickle", "rb") as f:
                    game_data = pickle.load(f)
                run_game(game_data)
            elif self.mID == 3:
                sys.exit(0)
            else:
                print("Wrong number")
    def command_battle(self, Game):
        if self.is_battle():
            if self.mID == 1:
                clear()
                return True

            elif self.mID == 2:
                clear()
                Game.character_menu()
            elif self.mID == 3:
                try:
                    with open("data.pickle", "wb") as f:
                        pickle.dump(Game, f, pickle.HIGHEST_PROTOCOL)
                        print("Game saved successfull")
                        os.system("pause")
                        clear()
                except pickle.PickleError:
                    print("Problem with saving game")  # need to improve this
            elif self.mID == 4:
                sys.exit(0)
#  main menu
m_new_game = Menu(1, "New game", "main")
m_load_game = Menu(2, "Load game", "main")
m_exit_game = Menu(3, "Exit", "main")
m_main_menu = {1:m_new_game, 2:m_load_game, 3:m_exit_game}

# battle menu
m_battle = Menu(1, "Start battle", "battle")
m_character = Menu(2, "Character menu", "battle")
m_save_game = Menu(3, "Save game", "battle")
m_exit_game = Menu(4, "Exit game", "battle")

m_battle_menu = {1:m_battle, 2:m_character, 3:m_save_game, 4:m_exit_game}

# clear display win/linux
def clear():
    os_clear = {"Linux" : "clear", "Windows" : "cls"}
    
    os.system(os_clear[platform.system()])

def pause():
    input("Hit any key to continue")

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
        while True:
            for obj in m_battle_menu.values():
                obj.print_menu_entry()
            game_menu = int(user_input("Game menu:"))
            if m_battle_menu[game_menu].command_battle(Game):
                break

        while True:  # battle sequence
            Game.info()
            print(Game.player.print_character_status())
            print(Game.opponent.print_character_status())
            print("\n")

            if not Game.battle_sequence():
                break
            pause()
            clear()
    print("\t---GAME OVER---")
    pause()

# main menu, creates or loads a game instance
def main():
    while True:
        for obj in m_main_menu.values():
            obj.print_menu_entry()

        menu_selection = int(user_input("Main menu:"))
        try:
            m_main_menu[menu_selection].command_main()
        except KeyError:
            print("Select a valid number")

if __name__ == "__main__":
    main()
