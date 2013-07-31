import random

def random_value():
    return random.randint(1, 10)

#FinalF characters

class Attribute(object):
    def __init__(self, atr_ID, atr_value, atr_name):
        self.atr_ID = atr_ID
        self.atr_value = atr_value
        self.atr_name = atr_name

    def name(self):
        return(self.atr_name)

    def value(self):
        return(self.atr_value)

    def ID(self):
        return(self.atr_ID)

    def reduce(self, amount):
        self.atr_value -= amount

    def improve(self):
        self.atr_value += 5

    def improve_for_newround(self):
        self.atr_value += random_value() + random_value()

    def is_ID(self, possible_id):
        return self.atr_ID == possible_id
            

class Character(object):

    def __init__(self, playername, npc, level, strength, vitality,
                    max_vitality, defense, dextery):


        """ set_attacks fills self.attacks with attack instance objects 
        set_attacks iterates over self.learned_abilitys which contains
        a list of dicts, each dict contains attack informations"""

        def set_attacks(self):
            self.attacks = {}
            for index, obj in enumerate(self.learned_attacks):
                self.attacks[index] = Attack(obj["name"],
                                            obj["damage_mod"],
                                            obj["cooldown"],
                                            obj["cooldown_counter"])
            return self.attacks

        # character properties
        self.npc = npc
        self.name = playername
        self.level = level  # base value 1
        self.current_attack_id = None

        # character status values
        self.strength = Attribute(1, 10, "Strength")  # base value 10
        self.vitality = Attribute(2, 100, "Vitality")  # base value 100
        self.max_vitality = Attribute(3, 100, "Vitality")  # base val 100
        self.defense = Attribute(4, 5, "defense")  # base value 5
        self.dextery = Attribute(5, 15, "dextery")  # base value 15
        self.combat_experience = 100  # base value 100
        self.exp = 70
        self.exp_levelup = 100
        self.attribute_points = 5

        # current abilitys
        self.learned_attacks = (punch, kick, metalfist, beamcanon, gundam_support)
        # list contains pre defined attacks (dicts)
        self.attacks = set_attacks(self)

        # base damage
        self.base_damage = int(self.strength.value() + (self.dextery.value() / 3) +
                            (self.combat_experience / 10))

    # character gets improved after each round, if he collected enough exp the
    # character reaches a new level and retrieves 5 attribute points which he 
    # can set
    def improve(self):
        self.strength.improve_for_newround()
        self.max_vitality.improve_for_newround()
        self.defense.improve_for_newround()
        self.dextery.improve_for_newround()
        self.vitality.atr_value = self.max_vitality.value()
        self.exp += 50

        if self.exp >= self.exp_levelup:
            self.exp -= self.exp_levelup
            self.exp_levelup += 20
            self.attribute_points += 5
            self.level += 1

    def macro_attributes(self):
        return(self.strength, self.max_vitality, self.defense, self.dextery)

    def improve_attribute(self, obj):
        self.attribute_points = 0
        obj.improve()

    #  index is the key of the attacks in the list of dicts "attacks"
    def print_attack_status(self):
        for index, attack in self.attacks.items():
            print("\t\t{0}: {1} cooldown: {2}/{3}".format(
                index, attack.name, attack.cooldown_counter,
                attack.cooldown))

    def print_character_status(self):
        return("\tName: {0} \t Vitality: {1}/{2}".format(
            self.name, self.vitality.value(), self.max_vitality.value()))

    def details(self, game_round):
        print("\n\tName: {0} \t\t Level: {1}".format(self.name, self.level))
        print("\tExp: {0}/{1} \t\t Round:".format(self.exp,
            self.exp_levelup, game_round))
        print("\n\t1: Strength: {0} \t 2: Vitality: {1}".format(
            self.strength.value(), self.max_vitality.value()))
        print("\t3: Dextery: {0} \t 4: Defense: {1}\n".format(self.dextery.value(),
            self.defense.value()))

    # print all attacks with "id, name"
    def print_attacks(self):
        for index, obj in self.attacks.items():
            print(index, obj.name)

    #  if the selected attack is usable set it to "self.current_attack"
    def select_attack_if_usable(self, choice):
        if choice in self.attacks.keys() and self.attacks[choice].is_usable():
            self.current_attack_id = choice
            return True
        else:
            return False

    #  write all usable skills in "available" and randomly pick on of them
    def random_attack(self):
        available = []
        for index, attack in self.attacks.items():
            if attack.is_usable():
                available.append(index)
        self.current_attack_id = random.choice(available)

    # set the selected attack on cooldown
    def set_attack_cooldown(self):
        self.attacks[self.current_attack_id].set_cooldown()

    # reduce all attacks cooldown for 1
    def reduce_attack_cooldowns(self):
        for attack_obj in self.attacks.values():
            attack_obj.reduce_cooldown()

    # check if character is defeated
    def defeated(self):
        return self.vitality.value() < 1

    # calculates damage: attack damge + character base damage
    def attack(self):
        return (self.attacks[self.current_attack_id].damage()
            + self.base_damage)

    # returns value of defense attribute
    def defend(self):
        return self.defense.value()

    def current_attack_name(self):
        return self.attacks[self.current_attack_id].attack_name()        
    
    # damage is the amout vitality will be reduced
    def reduce_vitality(self, damage):
        self.vitality.reduce(damage)

    def get_attribute_points(self):
        return self.attribute_points


class Attack(object):

    def __init__(self, name, damage_mod, cooldown, cooldown_counter):
        self.name = name
        self.damage_mod = damage_mod
        self.cooldown = cooldown
        self.cooldown_counter = cooldown_counter

    def reduce_cooldown(self):
        if self.cooldown_counter < self.cooldown:
            self.cooldown_counter += 1

    def set_cooldown(self):
        self.cooldown_counter -= self.cooldown + 1

    def is_usable(self):
        return self.cooldown_counter == self.cooldown

    def attack_name(self):
        return self.name

    def damage(self):
        return self.damage_mod

# attack information source
# later will be loaded from a file or something like that..

punch = {"name": "Punch", "damage_mod": 10, "cooldown": 1,
        "cooldown_counter": 1}
kick = {"name": "Kick", "damage_mod": 20, "cooldown": 1,
        "cooldown_counter": 1}
metalfist = {"name": "Metal Fist", "damage_mod": 30, "cooldown": 5,
            "cooldown_counter": 5}
beamcanon = {"name": "Beam Canon", "damage_mod": 40, "cooldown": 5,
            "cooldown_counter": 5}
gundam_support = {"name": "Gundam Support", "damage_mod": 50, "cooldown": 5,
            "cooldown_counter": 5}


#Generate name
def random_name():
    pre = ("Lord", "Hero", "Master", "Chief", "Leader", "Boss")
    name = ("Manfred", "Bubi", "Dödel", "Affenmensch", "Heinrich")
    title = ("the broken", "the stupid", "of somewhere")
    # "titel" is for higher levels... not implemented yet

    new_name = random.choice(pre) + " " + random.choice(name)
    return new_name
