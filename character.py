import random

def random_value():
    return random.randint(1, 10)

#FinalF characters


class Character():

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

        # base damage
        self.base_damage = int(self.strength + (self.dextery / 3) +
                            (self.combat_experience / 10))

    # character gets improved after each round, if he collected enough exp the
    # character reaches a new level and retrieves 5 attribute points which he 
    # can set
    def improve(self):
        self.strength += random_value() + random_value()
        self.max_vitality += random_value() + random_value()
        self.defense += random_value() + random_value()
        self.dextery += random_value() + random_value()
        self.vitality = self.max_vitality
        self.exp += 50

        if self.exp >= self.exp_levelup:
            self.exp -= self.exp_levelup
            self.exp_levelup += 20
            self.attribute_points += 5
            self.level += 1

    #  index is the key of the attacks in the list of dicts "attacks"
    def print_attack_status(self):
        for index, attack in self.attacks.items():
            print("\t\t{0}: {1} cooldown: {2}/{3}".format(
                index, attack.name, attack.cooldown_counter,
                attack.cooldown))

    def character_status(self):
        return("\tName: {0} \t Vitality: {1}/{2}".format(
            self.name, self.vitality, self.max_vitality))

    def details(self, game_round):
        print("\n\tName: {0} \t\t Level: {1}".format(self.name, self.level))
        print("\tExp: {0}/{1} \t\t Round:".format(self.exp,
            self.exp_levelup, game_round))
        print("\n\t1: Strength: {0} \t 2: Vitality: {1}".format(
            self.strength, self.max_vitality))
        print("\t3: Dextery: {0} \t 4: Defense: {1}\n".format(self.dextery,
            self.defense))

    # print all attacks with "id, name"
    def print_attacks(self):
        for index, obj in self.attacks.items():
            print(index, obj.name)

    #  if the selected attack is usable set it to "self.current_attack"
    def select_attack(self, choice):
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
        if self.vitality <= 0:
            return True
        else:
            return False

    # calculates damage: attack damge + character base damage
    def attack(self):
        return (self.attacks[self.current_attack_id].damage()
            + self.base_damage)

    # returns value of defense attribute
    def defend(self):
        return self.defense

    def current_attack_name(self):
        return self.attacks[self.current_attack_id].attack_name()        
    
    def reduce_vitality(self, damage):
        self.vitality -= damage

class Attack():

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
        if self.cooldown >= self.cooldown_counter:
            return True
        else:
            False

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
