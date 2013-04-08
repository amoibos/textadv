import random
random.seed(None)

def random_value():
    return random.randint(1, 10)

#FinalF characters


class NewCharacter():

    def __init__(self, playername, npc, level, strengh, vitality,
                    max_vitality, defense, dextery):

        # set_attacks fills self.attacks with attack instance objects 
        # set_attacks iterates over self.learned_abilitys which contains
        # a list of dicts, each dict contains attack informations

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
        self.strengh = strengh  # base value 10
        self.vitality = vitality  # base value 100
        self.max_vitality = max_vitality  # base value 100
        self.defense = defense  # base value 5
        self.dextery = dextery  # base value 15
        self.combat_experience = 100  # base value 100

        # current abilitys
        self.learned_attacks = (punch, kick, metalfist, beamcanon, gundam_support)
        # list contains pre defined attacks (dicts)
        self.attacks = set_attacks(self)
        self.abilitys = ["heal", "paralyze", "invisible"]  # some ability ideas
        # not implemented yet

        # base damage
        self.base_damage = int(self.strengh + (self.dextery / 3) +
                            (self.combat_experience / 10))

    def improve(self):
        self.level += 1
        self.strengh += random_value() + random_value()
        self.max_vitality += random_value() + random_value()
        self.defense += random_value() + random_value()
        self.dextery += random_value() + random_value()
        self.vitality = self.max_vitality

    def print_attacks(self):
        for index, obj in self.attacks.items():
            print(index, obj.name)

    def select_attack(self, choice):
        if choice in self.attacks.keys() and \
        self.attacks[choice].cooldown_counter == self.attacks[choice].cooldown:
            return True
        else:
            return False

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


#Generate Opponent
def random_name():
    pre = ("Lord", "Hero", "Master", "Chief", "Leader", "Boss")
    name = ("Manfred", "Bubi", "Dödel", "Affenmensch", "Heinrich")
    title = ("the broken", "the stupid", "of somewhere")
    # "titel" is for higher levels... not implemented yet

    def generate_name():
        new_name = random.choice(pre) + " " + random.choice(name)
        return new_name

    return generate_name()


#player = NewCharacter("Dude", False, 1, 10, 100, 10, 15, 100)
#player.print_attacks()
