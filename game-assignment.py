import os.path
import random

scenario = 'scenario.txt'
setting_off = 'setting-off.txt'
encounter = 'encounter.txt'
encounter_entry = 'encounter-entry.txt'
kitchen = 'kitchen.txt'
bedroom = 'bedroom.txt'
basement = 'basement.txt'
potion = 'potion.txt'
success_message = 'success-message.txt'
failure_message = 'failure-message.txt'

# opens the scenario.txt file if it exists

open_scenario = os.path.isfile(scenario)

if open_scenario == True:
    infile = open(scenario, 'r')
    read_file = infile.read()
    print(read_file)
else:
    print('The scenario.txt file does not exist.')

# opens the setting-off.txt file if it exists
open_setting_off = os.path.isfile(setting_off)

if open_setting_off == True:
    infile = open(setting_off, 'r')
    read_file = infile.read()
    print(read_file)
else:
    print('The setting-off.txt file does not exist.')

# opens the encounter.txt file if it exists
open_encounter = os.path.isfile(encounter)

if open_encounter == True:
    infile = open(encounter, 'r')
    read_file = infile.read()
    print(read_file)
else:
    print('The encounter.txt file does not exist.')

# this is the first decision from the player to open or flee the hut, answered by user input
while True:
    try:
        enter_or_flee = int(input("Would you like to open the door(1) or flee(2)?"))
        if enter_or_flee == 1:
            print ("You set your fears aside and enter the hut...")
            break
        elif enter_or_flee == 2:
            print ("You succumb to your fears and flee.")
            quit()
        else:
           print ("Please pick 1 or 2.")
           pass
    except ValueError:
        print("Please pick 1 or 2.")

# opens encounter-entry.txt file if it exists
open_encounter_entry = os.path.isfile(encounter_entry)

if open_encounter_entry == True:
    infile = open (encounter_entry, 'r')
    read_file = infile.read()
    print (read_file)

# this is the second decision from the player to search the messy table, answered by user input. if they search, they get the enchanted ring. if they don't, they don't get ring
while True:
    try:
        search_table = int (input ("Would you like to search the messy table? Yes(1) or No(2)"))
        if search_table == 1:
            print ("You search the messy table and find an Enchanted Ring, which gives you +1 on attacks.")
            # the ring grants +1 attack power
            enchanted_ring = 1
            break
        elif search_table == 2:
            print ("You ignore the table and look towards the doorways...")
            # the ring grants +0 attack power since they did not search
            enchanted_ring = 0
            break
        else:
            print ("Please pick 1 or 2.")
            pass
    except ValueError:
        print("Please pick 1 or 2.")

# this shows that the key has not been found and that gryla has not been defeated yet
chest_key = False
gryla_defeated = False
# this is the second decision from the player to choose the left door or the right door. the left door leads to the kitchen while the right leads to the bedroom
while True:
    kitchen_or_bedroom = int (input ("Would you like to go through the left(1) or right(2) door?"))
    if kitchen_or_bedroom == 1:
        print ("You walk up to the door on the left and push it open")

        # open kitchen.txt if it exists
        open_kitchen = os.path.isfile(kitchen)
        if open_kitchen == True:
            infile = open(kitchen, 'r')
            read_file = infile.read()
            print(read_file)
        else:
            print ("The kitchen.txt file does not exist.")

        # players must make a decision in the kitchen to search, go back, or go downstairs
        while True:
            search_goback_stairs = int(input("Would you like to search(1), go back to the previous room(2), or go down the stairs(3)?"))
            if search_goback_stairs == 1:
                print("You search the kitchen, but find nothing...")
            elif search_goback_stairs == 2:
                print("You return to previous room.")
                break
            elif search_goback_stairs == 3:
                if gryla_defeated == False:
                    print("You climb down the ladder, where you encounter Gryla")
                    break
                else:
                    print("You sealed off the stairwell already. There is no way back down the stairs.")
        # if gryla has not been defeated yet, it will open the basement.txt text file if it exists
        if gryla_defeated == False:
            open_basement = os.path.isfile(basement)
            if open_basement == True:
                infile = open(basement, 'r')
                read_file = infile.read()
                print(read_file)
            else:
                print("The basement.txt file does not exist.")
            # this shows that persuade and consider options have not been tried yet since they can only perform these actions once
            persuade = False
            consider = False
            # player must make a decision to attack, persuade, or consider gryla
            while True:
                attack_persuade_consider = int(input("Would you like to attack(1), persuade(2), or consider gryla more carefully(3)?"))
                dice_sides = 20
                first_dice_roll = random.randint(1, dice_sides)
                # the first dice roll determines how many hits it takes to defeat gryla
                if attack_persuade_consider == 1:
                    if first_dice_roll == 1:
                        total_hits_needed = 3
                    elif first_dice_roll >= 20:
                        total_hits_needed = 1
                    else:
                        total_hits_needed = 2
                    print("You need to hit Gryla", total_hits_needed, "times to defeat her.")
                    print("Gryla needs 2 hit twice to defeat you.")
                    # this shows how many hits that gryla and player start off with. 
                    hit_gryla = 0
                    hit_player = 0
                    # gryla will always only need to hit the player 2 times
                    kill_player_hits = 2
                    # this is the dice rolling loop that continues until player or gryla is defeated
                    while True:
                        random_dice = random.randint(1, dice_sides)
                        # if the player found the enchanted ring from the messy table, this is where it adds the +1 to all attacks
                        player_current_roll = random_dice + enchanted_ring
                        print("You roll a:", player_current_roll)
                        # player roll needs to be 12 or higher to hit gryla
                        if player_current_roll >= 12:
                            hit_gryla += 1
                            print("YOU HIT GRYLA")
                            # if player's hits towards gryla are equal to total hits needed, gryla is defeated and the player is brought back to the lobby
                            if hit_gryla == total_hits_needed:
                                print("You have defeated Gryla, you grab the key from her corpse and walk back upstairs, sealing the stairwell off behind you.")
                                print("You find yourself back in the lobby. Wasn't there a chest somewhere before?")
                                # if gryla is defeated, gryla defeated is true, which grants the player with the chest key
                                chest_key = True
                                gryla_defeated = True
                                break
                            else:
                                pass
                        else:
                            print("YOU MISSED")
                            pass
                        # after each player roll, gryla rolls as well unless she is defeated
                        # for attacking, the player reacts quickly, so gryla's rolls are always subtracted by 4
                        gryla_current_roll = random_dice - 4
                        print("Gryla rolls a:", gryla_current_roll)
                        if gryla_current_roll >= 12:
                            hit_player += 1
                            print("GRYLA HITS YOU")
                            # if gryla's hits toward player are equal to kill player hits, player is defeated, which displays the failure-message.txt if it exists
                            if hit_player == kill_player_hits:
                                open_failure_message = os.path.isfile(failure_message)
                                if open_failure_message == True:
                                    infile = open(failure_message, 'r')
                                    read_file = infile.read()
                                    print(read_file)
                                    quit()
                                else:
                                    print("The failure-message.txt file does not exist.")
                            else:
                                pass
                        else:
                            print("GRYLA MISSED")
                            pass
                    break
                # if the player wants to try persuading
                elif attack_persuade_consider == 2 and not persuade:
                    random_dice = random.randint(1, dice_sides)
                    player_dice_roll = random_dice
                    print("You roll a:", player_dice_roll)
                    gryla_dice_roll = random_dice + 4
                    print("Gryla rolls a:", gryla_dice_roll)
                    if player_dice_roll > gryla_dice_roll:
                        print("Gryla disappears and you obtain a key")
                        chest_key = True
                        gryla_defeated = True
                        break

                    else:
                        print("You failed to persuade gryla. your only option is to consider or attack.")
                    persuade = True
                # if the player wants to try considering
                elif attack_persuade_consider == 3 and not consider:
                    random_dice = random.randint(1, dice_sides)
                    player_dice_roll = random_dice
                    print("You roll a:", player_dice_roll)
                    gryla_dice_roll = random_dice - 2
                    print("Gryla rolls a:", gryla_dice_roll)
                    if player_dice_roll > gryla_dice_roll:
                        print("You see gryla is just unwell, cure her, and obtain the key.")
                        print("Gryla thanks you, leads you back to the lobby and tells you to make yourself at home while she makes tea.")
                        chest_key = True
                        gryla_defeated = True
                        break
                    else:
                        print("You failed to consider Gryla.")
                    consider = True
                else:
                    print("You can only attempt to persuade or consider Gryla once. Your only option left might be to attack.")

    elif kitchen_or_bedroom == 2:
        print ("You walk up to the door on the right and push it open.")

        # open bedroom.txt if it exists
        open_bedroom = os.path.isfile(bedroom)
        if open_bedroom == True:
            infile = open(bedroom, 'r')
            read_file = infile.read()
            print(read_file)
        else:
            print ("The bedroom.txt file does not exist.")

        while True:
            search_goback_stairs = int(input("Would you like to search(1), go back to the previous room(2), or attempt to open the locked chest(3)?"))
            if search_goback_stairs == 1:
                print("You search the bedroom, but find nothing...")
            elif search_goback_stairs == 2:
                print ("You return to previous room.")
                break
            elif search_goback_stairs == 3:
                if chest_key == True:
                    open_potion = os.path.isfile(potion)
                    if open_potion == True:
                        infile = open(potion, 'r')
                        read_file = infile.read()
                        print(read_file)
                    else:
                        print("The potion.txt file does not exist.")
                    open_success_message = os.path.isfile(success_message)
                    if open_success_message == True:
                        infile = open(success_message, 'r')
                        read_file = infile.read()
                        print(read_file)
                        quit()
                    else:
                        print("The success-message.txt file does not exist.")
                else:
                    print("You attempt to open the locked chest, but do not have a key. Maybe it's around somewhere?")
