import random

def random_value():
    return random.randint(1, 10)

#FinalF characters


class Character():

    def __init__(self, playername, npc, level, strength, vitality,
                    max_vitality, defense, dextery):

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

        # character status values
        self.strength = strength  # base value 10
        self.vitality = vitality  # base value 100
        self.max_vitality = max_vitality  # base value 100
        self.defense = defense  # base value 5
        self.dextery = dextery  # base value 15
        self.combat_experience = 100  # base value 100
        self.exp = 0
        self.exp_levelup = 100
        self.attribute_points = 0

        # current abilitys
        self.learned_attacks = (punch, kick, metalfist, beamcanon, gundam_support)
        # list contains pre defined attacks (dicts)
        self.attacks = set_attacks(self)
        self.abilitys = ["heal", "paralyze", "invisible"]  # some ability ideas
        # not implemented yet

        # base damage
        self.base_damage = int(self.strength + (self.dextery / 3) +
                            (self.combat_experience / 10))

        # set_attacks fills self.attacks with attack instance objects 
        # set_attacks iterates over self.learned_abilitys which contains
        # a list of dicts, each dict contains attack informations



    def improve(self):
        self.strength += random_value() + random_value()
        self.max_vitality += random_value() + random_value()
        self.defense += random_value() + random_value()
        self.dextery += random_value() + random_value()
        self.vitality = self.max_vitality

    #  index is the key of the attacks in the list of dicts "attacks"
    def print_attack_status(self):
        for index, attack in self.attacks.items():
            print("\t\t{0}: {1} cooldown: {2}/{3}".format(
                index, attack.name, attack.cooldown_counter,
                attack.cooldown))

    def character_status(self):
        return("""
            Name: {0}
            Vitality: {1}/{2}""".format(
                self.name, self.vitality,
                self.max_vitality))

    def print_attacks(self):
        for index, obj in self.attacks.items():
            print(index, obj.name)

    def select_attack(self, choice):
        if choice in self.attacks.keys() and \
        self.attacks[choice].cooldown_counter == self.attacks[choice].cooldown:
            return True
        else:
            return False

    #  write all ready skills in "available" and randomly pick on of them
    def random_attack(self):
        available = []
        for index, attack in self.attacks.items():
            if attack.cooldown_counter == attack.cooldown:
                available.append(index)
        return random.choice(available)

    def set_attack_cooldown(self, attack):
            self.attacks[attack].cooldown_counter -= \
            self.attacks[attack].cooldown + 1

    def reduce_attack_cooldown(self):
        # reducing cooldowns
        for obj in self.attacks.values():
            if obj.cooldown_counter < obj.cooldown:
                obj.cooldown_counter += 1


class Attack():

    def __init__(self, name, damage_mod, cooldown, cooldown_counter):
        self.name = name
        self.damage_mod = damage_mod
        self.cooldown = cooldown
        self.cooldown_counter = cooldown_counter

# attack information source
# later will be loaded from a file

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
