import character
import random
import platform
import os
import dialog

game_state = ""

def main():
    while True:
        #---setup---
        random.seed(None)

        #-environment-
        unexpected_error = "Unexpected error"
        prompt = ">>"

        def press_enter():
            dialog.msg("battle", "Press enter to continue")
            x = input(prompt)

        def main_menue():
            #dialog.cls()
            print("""
            --------------------------------------------------
            |                FINAL FIGHT
            |                  main menue
            | 1 New Game
            | 2 Load Game
            | 3 Exit
            |
            --------------------------------------------------
            """)

        def newgame():  # Story, Player name, character instances, call battle function
            dialog.cls()
            dialog.msg("text", ("You woke up in a dark chamber... your head hurts",
            "Can you remember your name?")) # no time for big story, sorry ;)

            while True:
                try:
                    player_name = input(str(prompt))
                    if len(player_name) >= 3:
                        break
                    else:
                        dialog.msg("text", "Name is too short")
                except ValueError:
                    dialog.msg("error", "Only letters and numbers")
                except:
                    dialog.msg("error", "error 1")

            player = character.Character(player_name, False, 1, 10, 100, 100, 5, 15)
                # Create player instance, set npc status False

            opponent = character.Character(character.random_name(), True,
                                            1, 10, 100, 100, 5, 15)
            #opponent_attack = character.attack_instantiate(opponent)
                # Create opponent instance, set npc status True

            dialog.cls()
            dialog.msg("text", ("So your name is.... {0}".format(player.name),
            "Move on if your ready for your", "+++Final Fight+++",
            "\"Imagine big Intro Logo here\"",
            "Press Enter to continue"))
            blank = input()  #im sure this isnt the best way...
            characters = (player, opponent)
            return characters

        def new_round(player, opponent):  # improv chars, rest vita, call battle function
            character.improve(opponent)
            opponent.name = character.random_name()
            player.vitality = player.max_vitality
            character.improve(player)

        def battle(player, opponent):
            round_count = 0
            global game_state
            print("game state:", game_state)

            def characters_status():  # returns a string of player attributes
                return ("{0} Vitality: {1}/{2}".format(
                    player.name, player.vitality, player.max_vitality),
                    "{0} Vitality: {1}/{2}".format(opponent.name, opponent.vitality,
                                                    opponent.max_vitality))

            def character_attacks_status(character):
            # returns a list containing:
            # strings of attacks with cooldown timer or "ready"
                attacks_status = []
                for index, obj in character.attacks.items():
                    if obj.cooldown_counter < obj.cooldown:

                        attacks_status.append("{0}: {1} cooldown {2}/{3}"
                                            .format(index, obj.name,
                                            obj.cooldown_counter, obj.cooldown))

                    elif obj.cooldown_counter == obj.cooldown:
                        attacks_status.append("{0}: {1} ready".format(index, obj.name))
                return attacks_status

            def random_attack(character): 
            # return the number of a random selected attack
                ready_skills = []
                for key, obj in character.attacks.items():
                    if obj.cooldown_counter == obj.cooldown:
                        ready_skills.append(key)
                selection = random.choice(ready_skills)
                return selection

            def check_defeated(character):  # check if char vitality <= 0
                if character.vitality <= 0:
                    return True

            def character_attack(selection, character, opponent):
            # check if pressed key is in attacks of character instance
            # check if attack is on cooldown
            # decrease vitality of opponent
            # set cooldowns
            # return damage value

                def damage_calc():
                    return character.base_damage + character.attacks[selection].damage_mod \
                            - opponent.defense

                def set_attack_cooldown():
                    character.attacks[selection].cooldown_counter -= \
                    character.attacks[selection].cooldown + 1

                    for obj in character.attacks.values():
                        if obj.cooldown_counter < obj.cooldown:
                            obj.cooldown_counter += 1

                while True:
                    if character.npc == True:

                        opponent.vitality -= damage_calc()
                        set_attack_cooldown()
                        return damage_calc()
                            

                    if character.npc == False:

                        while True:
                        # check if pressed key is in attacks of character instance:
                            if selection not in character.attacks:
                                print("Wrong Key")

                            # check if attack is on cooldown:
                            elif character.attacks[selection].cooldown_counter < \
                                character.attacks[selection].cooldown:
                                print("Skill is on cooldown")

                            # check if input is "empty":
                            elif selection == "":
                                print("No attack selected")

                            else: # if selection is correct exit loop
                                break

                            selection = int(input(prompt))

                        # if everything is okay the following happens
                        if selection in character.attacks and \
                        character.attacks[selection].cooldown_counter == \
                        character.attacks[selection].cooldown:

                            opponent.vitality -= damage_calc()
                            # decrease opponent vitality by the calcualted damage

                            set_attack_cooldown() # set cooldowns

                            return damage_calc()  #to display attack damage

                        else:
                            print("Something went wrong!")


            dialog.cls()
            while player.vitality or opponent.vitality <= 0:
            # battle sequence, damage calc,
                round_count += 1
                player.combat_experience += 1

                #player attacks
                dialog.msg("text", (characters_status(), "-", character_attacks_status(player), "-",
                            "Round {0}! Its your turn {1}".format(round_count, player.name),
                            "Level {0}".format(player.level)))
                while True:
                    try:
                        selection = int(input(prompt))
                        break
                    except ValueError:
                        dialog.msg("error", "Enter the number of an attack")

                damage = character_attack(selection, player, opponent)
                dialog.msg("battle", ("{0} hit {1} with a {2} and dealed {3} damage"
                            .format(player.name, opponent.name, player.attacks[selection].name, damage)))

                if check_defeated(opponent) is True:
                    game_state = "new round"
                    dialog.msg("battle", ("{0} has been defeated by {1} press enter to continue".format(opponent.name, player.name)))
                    press_enter()
                    break
                
                # enemy attacks
                selection = random_attack(opponent)
                damage = character_attack(selection, opponent, player)
                dialog.msg("battle", ("{0} hit {1} with a {2} and dealed {3} damage"
                            .format(opponent.name, player.name, opponent.attacks[selection].name, damage)))
                press_enter()

                if check_defeated(player) is True:
                    game_state = "defeated"
                    dialog.msg("battle", ("{0} has been defeated by {1} press enter to continue".format(player.name, opponent.name)))
                    x = input(prompt)
                    break
                #dialog.cls()
            print("battle loop")

        if game_state == "" or game_state == "defeated":
            main_menue()
            while True:
                try:
                    input_menu = int(input(prompt))
                    if input_menu == 1:
                        player, opponent = newgame()
                        battle(player, opponent)  
                        break               
                    if input_menu == 2:
                        pass
                    if input_menu == 3:
                        pass
                    if input_menu == 4:
                        pass
                except ValueError:
                    dialog.msg("error", "Input is not in between 1 - 3")
        elif game_state == "new round":
            new_round(player, opponent)
            battle(player, opponent)
            

if __name__ == "__main__":
    main()
