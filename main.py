import character
import random
import itertools
import os
import platform


random.seed()


def main():
    def clear():
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")

    class NewGame():
        def __init__(self):
            self.player = character.NewCharacter("Dude",
            False, 1, 10, 100, 100, 15, 100)

            self.opponent = character.NewCharacter(character.random_name(),
            True, 1, 10, 120, 120, 15, 50)

            self.round = 1
            self.state = "running"  # running, over, new

        #  check if a character has been defeated, initiate new round
        def check_defeated(self):
            if self.player.vitality <= 0:
                print("{0} has been defeated by {1}".format(self.player.name,
                self.opponent.name))
                game.state = "over"
                return True

            elif self.opponent.vitality <= 0:
                game.round += 1
                print("{0} has been defeated by {1}, prepare for round {2}"
                    .format(self.opponent.name, self.player.name, game.round))
                game.player.improve()
                game.opponent.improve()
                game.opponent.name = character.random_name()
                return True

        def info(self):
            print("-------------------------------------------------------")
            print("Round: {0}, Game state: {1}, Player: {2}, Opponent: {3}"
                .format(self.round, self.state, self.player.name,
                self.opponent.name))
            print("-------------------------------------------------------")

        def print_character_status(self):
            print("""
                Name: {0} \t\t Name: {1}
                Vitality: {2}/{3} \t Vitality: {4}/{5} \n""".format(
                    self.player.name, self.opponent.name, self.player.vitality,
                    self.player.max_vitality, self.opponent.vitality,
                    self.opponent.max_vitality))

        #  index is the key of the attacks in the list of dicts "attacks"
        def print_attack_status(self, character):
            for index, attack in character.attacks.items():
                print("\t\t{0}: {1} cooldown: {2}/{3}".format(
                    index, attack.name, attack.cooldown_counter,
                    attack.cooldown))

        #  write all ready skills in "available" and randomly pick on of them
        def random_attack(self):
            available = []
            for index, attack in self.opponent.attacks.items():
                if attack.cooldown_counter == attack.cooldown:
                    available.append(index)
            return random.choice(available)

        # ask player for attack input, check input, check cooldowns
        def attack_selection(self):
            while True:
                while True:
                    try:
                        selection = int(input("Attack:"))
                        break
                    except ValueError:
                        print("Wrong input, enter a number")
                if self.player.select_attack(selection) is True:
                    return selection
                else:
                    continue

        def set_attack_cooldown(self, character):
            # setting cooldowns
            for obj in character.attacks.values():
                if obj.cooldown_counter < obj.cooldown:
                    obj.cooldown_counter += 1
                else:
                    continue

    while True:

        print("""
            1 New game
            2 Load game
            3 Exit""")

        menu_selection = int(input("Menu:"))
        if menu_selection == 1:
            clear()
            game = NewGame()

            while True:
                if game.state == "over":
                    break
                else:
                    pass

                game.info()
                game.print_character_status()
                game.print_attack_status(game.player)

                #  PLAYER SCENE
                #  player attack input
                selection = game.attack_selection()

                #  set selected skill on cooldown
                game.player.attacks[selection].cooldown_counter -= \
                game.player.attacks[selection].cooldown + 1

                #  damage caluclation
                damage = ((game.player.attacks[selection].damage_mod +
                    game.player.base_damage) - game.opponent.defense)

                game.opponent.vitality -= damage

                #  text output
                print("You attacked with a {0} and dealed {1} damage".format(
                    game.player.attacks[selection].name, damage))

                #  set cooldowns
                game.set_attack_cooldown(game.player)

                if game.check_defeated() is True:
                    continue

                #  OPPONENT SCENE
                #  select random attack
                attack = game.random_attack()

                #  set selected skill on cooldown
                game.opponent.attacks[attack].cooldown_counter -= \
                    game.opponent.attacks[attack].cooldown + 1

                #  damage calculation
                damage = (
                    (game.opponent.attacks[attack].damage_mod +
                        game.opponent.base_damage) - game.player.defense)

                game.player.vitality -= damage

                #  text output
                print("{0} attacked with {1} and dealed {2} damage".format(
                    game.opponent.name, game.opponent.attacks[attack].name,
                    damage))

                #  set cooldowns
                game.set_attack_cooldown(game.opponent)

                if game.check_defeated() is True:
                    continue

                x = input("hit enter to continue")
                clear()
            print("game over: 1")
        else:
            print("exit ctrl + c")
    print("ctrl + c to exit")

if __name__ == "__main__":
    main()
