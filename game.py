import character

class Game():
    def __init__(self):
        self.player = character.Character("Dude", 
            False, 1, 10, 100, 100, 15, 100)

        self.opponent = character.Character(character.random_name(), 
            True, 1, 10, 120, 120, 15, 50)

        self.round = 1
        self.state = "running" 

    #  check if a character has been defeated, initiate new round
    def defeated(self):
        if self.player.vitality <= 0:
            print("{0} has been defeated by {1}".format(self.player.name,
                self.opponent.name))
            self.state = "over"
            return True

        elif self.opponent.vitality <= 0:
            self.round += 1
            print("{0} has been defeated by {1}, prepare for round {2}"
                .format(self.opponent.name, self.player.name, self.round))
            
            self.player.improve()
            self.player.exp += 50

            #  check player exp
            if self.player.exp >= self.player.exp_levelup:
                self.player.exp -= self.player.exp_levelup
                self.player.exp_levelup += 20
                self.player.attribute_points += 5
                self.player.level += 1

            self.opponent.improve()
            self.opponent.name = character.random_name()
            self.state = "newround"
            return True

    def info(self):
        print("\t==========================================================")
        print("Round: {0} | Game state: {1} | Player: {2} | Opponent: {3}"
            .format(self.round, self.state, self.player.name,
            self.opponent.name))
        print("\t__________________________________________________________\n")

    def damage_calc(self, attack):
                return((self.player.attacks[attack].damage_mod +
                    self.player.base_damage) - self.opponent.defense)


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

    def character_menu(self):
        print("""
            Name: {0} \t Level: {1}
            Round: {2} \t Points: {3}
            \tExp:{4}/{5}""".format(self.player.name,
                self.player.level, self.round,
                self.player.attribute_points, self.player.exp,
                self.player.exp_levelup))

        print("\n What you want to improve?")
        print("""
            1: Strength: {0} \t 2: Vitality: {1}
            3: Dextery: {2} \t 4: Defense: {3}
            \t\t5: exit\n""".format(self.player.strength,
                self.player.max_vitality, self.player.dextery,
                self.player.defense))
        while True:
            if self.player.attribute_points >= 5:
                try:
                    char_menu_input = int(input("Char attribute:"))
                except ValueError:
                    print("Enter a number")                            
                if char_menu_input == 1:
                    self.player.strength += 5
                    self.player.attribute_points -= 5
                    break
                elif char_menu_input == 2:
                    self.player.vitality += 5
                    self.player.attribute_points -= 5
                    break
                elif char_menu_input == 3:
                    self.player.dextery += 5
                    self.player.attribute_points -= 5
                    break
                elif char_menu_input == 4:
                    self.player.defense += 5
                    self.player.attribute_points -= 5
                    break
                elif char_menu_input == 5:
                    break
                else:
                    print("Select from 1 - 5")
            else:
                print("No points left")
                break

    def save(self):
        pass
