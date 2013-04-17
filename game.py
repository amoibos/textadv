import character
import os
from main import clear
from main import pause
from main import user_input


class CreateGame():
    def __init__(self):
        self.player = character.Character("Dude",
            False, 1, 10, 100, 100, 15, 100)

        self.opponent = character.Character(character.random_name(),
            True, 1, 10, 120, 120, 15, 50)

        self.round = 1
        self.state = "running"

    # check if a character has been defeated, initiate new round or return to
    # main menu
    def battle_end(self):
        if self.player.defeated():
            print("{0} has been defeated by {1}".format(self.player.name,
                self.opponent.name))
            self.state = "over"
            return True

        elif self.opponent.defeated():
            self.round += 1

            print("{0} has been defeated by {1}, prepare for round {2}"
                .format(self.opponent.name, self.player.name, self.round))

            self.player.improve()
            self.opponent.improve()
            self.opponent.name = character.random_name()
            self.state = "newround"
            return True
        else:
            return False

    # prints some "horizontal" infos about the current game
    def info(self):
        print("\t==========================================================")
        print("Round: {0} | Game state: {1} | Player: {2} | Opponent: {3}"
            .format(self.round, self.state, self.player.name,
            self.opponent.name))
        print("\t__________________________________________________________\n")

    # calculates damge, attack - defense
    def damage_calc(self, npc):
        if not npc:
                return self.player.attack() - self.opponent.defend()
        elif npc:
            return self.opponent.attack() - self.player.defend()
        else:
            print("Error in function damage_calc")

    # ask player for attack input, check input if usable
    def user_attack_selection(self):
        while True:
            try:
                selection = int(input("Attack:"))
                if self.player.select_attack_if_usable(selection):
                    break
                elif selection == 1337:
                    self.player.reduce_attack_cooldowns()
            except ValueError:
                print("Enter a number")

    def character_menu(self):  # need to be improved
        #self.player.details(self.round)

        for obj in self.player.macro_attributes():
            print("{0}: {1}: {2}".format(obj.ID(), obj.name(), obj.value()))
        print("\nYou have {0} Points left".format(self.player.get_attribute_points()))

        while True:
            if self.player.attribute_points >= 5:
              selection = user_input("Character attribute:")
              for obj in self.player.macro_attributes():
                if obj.is_ID(selection):
                    self.player.improve_attribute(obj)
                    break
            else:
                pause()
                clear()
                break

    def battle_sequence(self):

        # player battle sequence
        self.player.print_attack_status()
        self.user_attack_selection()
        self.player.set_attack_cooldown()
        # if player is attacking, npc = False, means its not an npc
        damage = self.damage_calc(False)
        self.opponent.reduce_vitality(damage)
        print("You attacked with a {0} and dealed {1} damage".format(
            self.player.current_attack_name(), damage))
        self.player.reduce_attack_cooldowns()
        if self.battle_end():
            return False

        # opponent battle sequence
        self.opponent.random_attack()
        self.opponent.set_attack_cooldown()
        damage = self.damage_calc(True)
        self.player.reduce_vitality(damage)
        print("{0} attacked you with a {1} and did {2} damage to you".format(
            self.opponent.name, self.opponent.current_attack_name(), damage))
        self.opponent.reduce_attack_cooldowns()
        if self.battle_end():
            return False
        else:
            return True
