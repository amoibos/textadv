import character
import random
import itertools
import os
import platform
import pickle
import game
import sys

def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


def main():               
    
    def run(Game):
        while True:
            if Game.state == "over":
                break
            else:
                pass

            print("1 Battle")
            print("2 Character menu")
            print("3 Save Game")
            print("4 Exit Game")
            while True:
                try:
                    Game_menu = int(input("Game menu:"))
                    break
                except ValueError:
                    print("Enter a number")
            if Game_menu == 1:
                pass
            elif Game_menu == 2:
                Game.character_menu()
                continue
            elif Game_menu == 3:
                try:
                    with open("data.pickle", "wb") as f:
                        pickle.dump(Game, f, pickle.HIGHEST_PROTOCOL)
                        print("Game saved successfull")
                except:
                    print("Problem with saving game")  # need to improve this
                continue
            elif Game_menu == 4:
                sys.exit(0)


            while True:
                Game.info()
                print("\tName: {0}\t\tName: {1}".format(Game.player.name,
                    Game.opponent.name))
                print("\tVitality: {0}/{1}\tVitality:{2}/{3}\n".format(
                    Game.player.vitality, Game.player.max_vitality,
                    Game.opponent.vitality, Game.opponent.max_vitality))

                Game.player.print_attack_status()

                #  PLAYER SCENE
                #  player attack input
                selection = Game.attack_selection()

                #  set selected skill on cooldown
                Game.player.set_attack_cooldown(selection)

                #  damage caluclation
                damage = Game.damage_calc(selection)
                Game.opponent.vitality -= damage

                #  text output
                print("You attacked with a {0} and dealed {1} damage".format(
                    Game.player.attacks[selection].name, damage))

                #  reduce cooldown of each attack
                Game.player.reduce_attack_cooldown()

                #  if ("opponent") defeated is True Game.state == ""
                #  means break out of "battle loop"
                if Game.defeated() is True:
                    break

                #  OPPONENT SCENE
                #  select random attack
                attack = Game.opponent.random_attack()

                #  set selected skill on cooldown
                Game.opponent.set_attack_cooldown(attack)

                #  damage calculation
                damage = (
                    (Game.opponent.attacks[attack].damage_mod +
                        Game.opponent.base_damage) - Game.player.defense)

                Game.player.vitality -= damage

                #  text output
                print("{0} attacked with {1} and dealed {2} damage".format(
                    Game.opponent.name, Game.opponent.attacks[attack].name,
                    damage))

                #  set cooldowns
                Game.opponent.reduce_attack_cooldown()

                if Game.defeated() is True:
                    break

                x = input("hit enter to continue")
                clear()
        print("Game over: 1")

    while True:

        print("""
            1 New Game
            2 Continue Game
            4 Exit""")
        while True:
            try:
                menu_selection = int(input("Menu:"))
                break
            except ValueError:
                print("Enter a number")

        if menu_selection == 1:
            clear()
            game_session = game.Game()
            run(game_session)
        elif menu_selection == 2:
            with open("data.pickle", "rb") as f:
                game_data = pickle.load(f)
            run(game_data)
        elif menu_selection ==3:
            print("There is no 3!")


        else:
            print("exit ctrl + c")
    print("ctrl + c to exit")

if __name__ == "__main__":
    main()
