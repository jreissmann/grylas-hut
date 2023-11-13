import os.path
scenario = 'scenario.txt'
setting_off = 'setting-off.txt'
encounter = 'encounter.txt'
encounter_entry = 'encounter-entry.txt'
kitchen = 'kitchen.txt'
bedroom = 'bedroom.txt'
basement = 'basement.txt'

# this checks and displays the first text file, which is the scenario file
open_scenario = os.path.isfile(scenario)

if open_scenario == True:
    infile = open(scenario, 'r')
    readFile = infile.read()
    print(readFile)
else:
    print('Scenario file does not exist')

# this checks and displays the second text file, which is the setting off file
open_setting_off = os.path.isfile(setting_off)

if open_setting_off == True:
    infile = open(setting_off, 'r')
    readFile = infile.read()
    print(readFile)
else:
    print('Setting Off file does not exist')

# this checks and displays the third text file, which is the encounter file
open_encounter = os.path.isfile(encounter)

if open_encounter == True:
    infile = open(encounter, 'r')
    readFile = infile.read()
    print(readFile)
else:
    print('Encounter file does not exist')

# this is the first decision from the player, answered by user input
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

#this checks and displays the fourth text file, which is the encounter-entry file
open_encounter_entry = os.path.isfile(encounter_entry)

if open_encounter_entry == True:
    infile = open (encounter_entry, 'r')
    readFile = infile.read()
    print (readFile)

#this is the second decision from the player to search the messy table, answered by user input
while True:
    try:
        search_table = int (input ("Would you like to search the messy table? Yes(1)/No(2)"))
        if search_table == 1:
            print ("You search the messy table and find an Enchanted Ring, which gives you +1 on attacks.")
            enchanted_ring = True
            break
        elif search_table == 2:
            print ("You ignore the table and look towards the doorways...")
            enchanted_ring = False
            break
        else:
            print ("Please pick 1 or 2.")
            pass
    except ValueError:
        print("Please pick 1 or 2.")

#this is the second decision from the player, answered by user input
while True:
    kitchen_or_bedroom = int (input ("Would you like to go through the left(1) or right(2) door?"))
    if kitchen_or_bedroom == 1:
        print ("You walk up to the door on the left and push it open")

        # open kitchen.txt if it exists
        open_kitchen = os.path.isfile(kitchen)
        if open_kitchen == True:
            infile = open(kitchen, 'r')
            readFile = infile.read()
            print(readFile)
        else:
            print ("The file does not exist.")

        # players must make a decision in the kitchen
        while True:
            search_goback_stairs = int(input("Would you like to search(1), go back to the previous room(2), or go down the stairs(3)?"))
            if search_goback_stairs == 1:
                print("You search the kitchen, but find nothing...")
            elif search_goback_stairs == 2:
                print("You return to previous room.")
                gryla = False
                break
            elif search_goback_stairs == 3:
                print("You climb down the ladder, where you encounter Gryla")
                gryla = True
                break
        if gryla == True:
            open_basement = os.path.isfile(basement)
            if open_basement == True:
                infile = open(basement, 'r')
                readFile = infile.read()
                print(readFile)

            persuade = False
            consider = False
            while True:
                attack_persuade_consider = int(input("Would you like to attack(1), persuade(2), or consider gryla more carefully(3)?"))
                if attack_persuade_consider == 1:
                    print("attack")
                elif attack_persuade_consider == 2 and not persuade:
                    persuade = True
                elif attack_persuade_consider == 3 and not consider:
                    consider = True
                else:
                    print("All other methods have failed. It seems like your only option is to attack Gryla now")
        else:
            pass

    elif kitchen_or_bedroom == 2:
        print ("You would up to the door n the right and push it open")

        # open bedroom.txt if it exists
        open_bedroom = os.path.isfile(bedroom)
        if open_bedroom == True:
            infile = open (bedroom, 'r')
            readFile = infile.read()
            print (readFile)
        else:
            print ("The file does not exist.")

        while True:
            search_goback_stairs = int(input("Would you like to search(1), go back to the previous room(2), or attempt to open the locked chest(3)?"))
            if search_goback_stairs == 1:
                print("You search the bedroom, but find nothing...")
            elif search_goback_stairs == 2:
                print ("You return to previous room.")
                break
            elif search_goback_stairs == 3:
                print ("You attempt to open the locked chest, but it's locked. Maybe there's a key somewhere?")

print("u got this far")
