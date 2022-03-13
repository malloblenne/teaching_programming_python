# Challenge

# Write a text based D&D 5e fighting game
# You are a swordman and you kill goblins
# Goblins spawns infinitely
# How many can you kill before falling death?
# you roll the dice by writing "r" for roll

# Reference

# see first page of https://media.wizards.com/downloads/dnd/StarterSet_Charactersv2.pdf
# your swordman has 17 Armour class, +3 modifier strength, 12 hit points, attacks with great axe +5 attack bonus 1d12 +3 damage, initiative -1
# general rules https://media.wizards.com/2020/dnd/downloads/dnd_starter_rulebook.pdf
# goblin page https://www.aidedd.org/dnd/monstres.php?vo=goblin
# goblin has 15 armour class,  -1 str, attack with scimitar 1d6+2 +4 to hit hit points 2d6 (initiative is with dex, so +2)

# how to fight:
# - roll 1d20 for initiatives for player and monster and apply modifier
# - one of the two starts, if user then type 'r'
# - roll 1d20 + attack modifier, against armour class (extra rule: if result of die is 20, then critical, extra die for damage)
# - if it hits, roll for damages

#Example output:

# write hero name: 'Jurgen the slasher'
# #1 A new Goblin appears
# Initiatives, 'Jurgen the slasher' starts first
# 'r'
# 'Jurgen the slasher' hits
# 'r'
# 'Jurgen the slasher' does 4 damages #even better if you make something like little, medium a lot and you hide the number
# Goblin is (lightly/medium/severely wounded)
# 'Goblin' misses hit
# 'Jurgen the slasher' hits
# 'r'
# 'Jurgen the slasher' does 12 damages #even better if you make something like little, medium a lot and you hide the number
# Goblin is dead
# #2 A new Goblin appears
# ....
# 'Jurgen the slasher' is defeated
# We all remember the great hero 'Jurgen the slasher' who killed X goblins!!
#  Game over!




# Extras
# 1) instead of typing, your fighter fights automatically, i.e., rolls automatically the dice
# 2) health potion spawns after you kill the goblin with a probabiliy of 25%. The potion heals 1d8 (Note your hitpoints shouldn't increase more than your max)
# 3) your experience increase, and you go to new levels. When you reach a new level you roll to increase your hit point

from colorama import Fore
import random
print('                                       ')
print('                                        ')
print(Fore.RED + 'PATH OF PERIL: a Dungeons & Dragons Adventure Game') 
print('                                                            ') 
print(Fore.BLUE + '    _,. ')
print(Fore.BLUE + '    ,` -.) ')
print(Fore.BLUE + '   ( _/-\\-._ ')
print(Fore.BLUE + '  /,|`--._,-^|            ,   ' )           
print(Fore.BLUE + '  \_| |`-._/||          ,"|    ')
print(Fore.BLUE + '    |  `-, / |         /  /      ')
print(Fore.BLUE + '    |     || |        /  /      ')
print(Fore.BLUE + '     `r-._||/   __   /  /       ')
print(Fore.BLUE + ' __,-<_     )`-/  `./  /        ')
print(Fore.BLUE + '  \   `---"   \   /  /         ' )
print(Fore.BLUE + '    |           |./  /          ')
print(Fore.BLUE + '    /           //  /           ')
print(Fore.BLUE + '\_/" \         |/  /            ')
print(Fore.BLUE + ' |    |   _,^-"/  /             ')
print(Fore.BLUE + ' |    , ``  (\/  /_             ')
print(Fore.BLUE + '  \,.->._    \X-=/^             ')
print(Fore.BLUE + '  (  /   `-._//^`                ')
print(Fore.BLUE + '   `Y-.____(__}                  ')
print(Fore.BLUE + '    |     {__)                   ')
print(Fore.BLUE + '          ()                     ')
s = input (Fore.YELLOW + 'Press S to start: ')

print(Fore.WHITE +'You are Jurgen Orkslasher fearless warrior on a quest to find the sacred stone of Mar Burlak.')
print('With this stone you will be able to return to the king of the realms and ask for the hand of his beautiful yet slightly autistic daughter.')
print('You have searched the lands high and low for any clues on where to find the stone.')
print('Finally, in a small tavern you come across on old man who tells you that he knows where the stone is, but he is unable to talk because of his dry throat.')
print(Fore.GREEN +'Will you buy him a beer?')
beer = input(Fore.YELLOW + 'Yes or No: ')
beer = str(beer)
if beer == 'No':
    print(Fore.WHITE + 'The stench of alcohol fills your nose. You become annoyed and tell him to bugger off. You tell him that he should bother someone else with his fairytales.')
    print('The old man looks at you angrily. "I curse you Jurgen Orkslayer! May you never find success and die a stupid death!"')
    print('Your hand reaches towards your sword, you hesitate for a moment and decide to let the old fool live. ')
    print('You leave the tavern and walk towards to inn where you are staying.') 
    print(' Just when you want to cross the road, you lose your balance on something slippery.')
    print(Fore.GREEN + 'Your legs are about to give out but you see someone standing next to you. Will you grab on to this person for support?')
    save = input(Fore.YELLOW + 'Yes or No: ')
    save = str(save)
    if save == 'No':
        print(Fore.WHITE + 'Even though you try to stay on your feet, your legs slip from under you and you crash the road.')
        print('Just as you crash on the road a horse comes speeding down the road. The last thing you see is a fast moving hoove approaching your face.')
        print('That night, the way your head exploded like a melon is the talk of the town.')
        print(Fore.RED + 'Game Over')  
        exit()
    if save == 'Yes':
        print(Fore.WHITE + 'Just as you are about to fall, you manage to grab the person standing next to you.')
        print('The person stands firm as a rock and you manage to keep standing.')
        print('You turn to thank to stranger. When you turn around you view is filled with a broad and very muscular chest covered with furs.')
        print('Your eyes move up for what seems like ages until you see a bg bearded face. A face that seems to be very unhappy with the situation.')
        print('Your mouth opens to thank him, but before you get to finish, you see a gigantic broadsword coming your way that you cannot dodge.')
        print('That evening, the way you were decapitated with grace by the huge barbarian is the talk of the town.')
        print(Fore.RED + 'Game Over')
        exit()
if beer == 'Yes':
    print(Fore.WHITE + 'You gesture the barkeep to give the old man a beer. The both of you sit down at a table in a quiet corner.')
    print(Fore.WHITE + 'The old man tells you that he used to be a royal guard. He was part of the escort that was supposed to tranport the stone to royal cathedral.')
    print(Fore.WHITE + 'When they passed through the old woods, they were ambushed by a horde of goblins. The old man seems to stare into the past while he tells you what happened.')
    print(Fore.WHITE + 'He tells you that it was a short but intense fight. The goblins outnumbered the guards and the goblins slaugtered all the guards.')
    print(Fore.WHITE + 'He himself took a hit to the head with a club and he passed out. The amount of blood on his head must have given the goblins the impression that he died.')
    print(Fore.WHITE + 'After what seemed like hours he wakes up just in time for the goblins to make it towards the weird goat shaped mountain nearby.')
    print(Fore.WHITE + 'They had taken the stone with them he tells you. Goblins are not known to move far from their lair, so there is a good chance that they are still there with the stone.')
    print(Fore.WHITE + 'You thank him for the information and buy him another round before returning to your horse to go to the mountain the old man told you about.')
    print('                                                                                                                                   ')
print(Fore.WHITE + 'A local guides you to the mysterious looking mountain. Upon arriving at the mountain you do not see any entrances.')
print(Fore.WHITE + 'The guide tells you that legend has it that the goblins that live there have protected the entrance with sneaky traps and dark magic.')
print(Fore.WHITE + 'They also have hidden the entrance and rumour has it that it will only open if the correct password is given.') 
print('                                                                                                                               ')
print(Fore.WHITE + 'You thank the guide and pay him. The guide wishes you the best of luck and warns you that you should be careful.')
print(Fore.WHITE + 'You begin to inspect the mountain side to see if you can identify some kind of crack or openening. On the far side of the mountain you discover some etchings in the wall.')
print(Fore.WHITE + 'The etchings are crude and in childish handwriting, but you can translate it.')
print(Fore.BLUE + 'For all you stupid idiots that keep forgetting the password: What consumes oxygen, eats and grows but will never be alive?')
print('                                                                                                                                 ')
answer = input(Fore.GREEN + 'The answer to the riddle is: ')
answer = str(answer)
if answer == 'Fire':
        print(Fore.WHITE + 'You loudly proclaim FIRE! The mountain starts shaking and an entrance appears out of nowhere.')
if answer != 'Fire':
    death1 = random.randint (1,6)
    death1 = int(death1)
    if death1 == 1:
        print(Fore.WHITE + 'You hear a loud noise coming from the top of the mountain. You look up and see multiple shapes rapidly falling towards you.')
        print(Fore.WHITE + 'You try to get out of the way, but before you manage to take on step, the objects hit you.')
        print(Fore.WHITE + 'The impact mortally wounds you. The last thing you see is lots of green and lots of teeth....')
        print(Fore.WHITE + 'You die wondering how the hell they managed to get crocodiles on top of that mountain..')
        print(Fore.RED + 'Game Over')
        exit()
    death2 = random.randint (1,6)
    death2 = int(death2)
    if death2 == 2:
        print(Fore.WHITE + 'The front of the cave begins to move. You knew you were smart enough to solve the riddle while the front of the cave seems to open.')
        print(Fore.WHITE + 'This was your last thought as the front of the cave moves enormously fast towards you, squishing you instantly on impact.')
        print(Fore.RED + 'Game Over')
        exit()
    death3 = random.randint (1,6)
    death3 = int(death3)
    if death3 == 3:
        print(Fore.WHITE + 'Fully confident that you answered correctly, you wait for the cave to open. Slowly, but surely the cave open up..... With a brisk step you enter the cave.')
        print(Fore.WHITE + 'Feeling full of energy you take a deep breath in order to take in your surroundings. You did not hear the low sissing noice coming out of the wall...')
        print(Fore.WHITE + 'The first thing you notice is a slight tickling feeling in your throat. Within seconds your throat begins to hurt and fill up with fluids.')
        print(Fore.WHITE + 'You start coughing heavily and your nose is starting to bleed. You feel weak and fall on the floor.') 
        print(Fore.WHITE + 'You are coughing up chunks which you realise are pieces of your lungs.')
        print(Fore.WHITE + 'A knight stumbles over your remains 6 years later, just before he also gets hit with the poisonous gas.')
        print(Fore.RED + 'Game Over')
        exit()
    death4 = random.randint (1,6)
    death4 = int(death4)
    if death4 == 4:
        print(Fore.WHITE + 'The moment you have spoken the password out loud, all you can see is a bright flash.') 
        print(Fore.WHITE + 'The next moment you can only see clear blue skies all around you.')
        print(Fore.WHITE + 'You are not in the cave anymore, but up in the sky somewhere. You look below and you are a few hundred meters above the ground.')
        print(Fore.WHITE + 'While you are falling you notice that the height is not the worst....you are falling towards the opening of a lava filled volcano.')
        print(Fore.WHITE + 'Your last thought as your body hits the lava is whether the fall or the lava killed you....')
        print(Fore.RED + 'Game Over')
        exit()
    death5 = random.randint (1,6)
    death5 = int(death5)
    if death5 == 5:
        print(Fore.WHITE + 'The password must have been correct because the cave entrance opens.')
        print(Fore.WHITE + 'The light that comes from the cave is almost golden, the cave must be filled with riches.')
        print(Fore.WHITE + 'You hear a beautiful female voice calling to you, asking you to enter the cave.') 
        print(Fore.WHITE + 'The voice is enchanting and you immediately take a step towards the entrance')
        print(Fore.WHITE + 'At least, you try to take a step. You cannot seem to move your feet.') 
        print(Fore.WHITE + 'It feels like they are made of stone. You feel your legs with your hands, but they feel normal.')
        print(Fore.WHITE + 'Nevertheless you are unable to move. You start screaming for help while you still hear the enchanting voice begging you to enter the cave.')
        print(Fore.WHITE + 'After a while you cannot scream anymore, you have lost your voice.')
        print(Fore.WHITE + 'You can feel birds picking on the flash of your face, but your are unable to scare them away with your arms.')
        print(Fore.WHITE + 'In the end it takes 4 days for you to die. During that whole time you see golden light and hear the beautiful voice.')
        print(Fore.WHITE + 'The strange magic that held you in place continues to do so after your death.') 
        print(Fore.WHITE + 'Your skeleton that is still standing in its boots becomes sort of a local tourist attraction: Come see immovable, standing skeletal warrior!')
        print(Fore.RED + 'Game Over')
        exit()
    death6 = random.randint (1,6)
    death6 = int(death6)
    if death6 == 6:
        print(Fore.WHITE + 'Slowly but surely the cave entrance opens. That riddle was no challenge for your superior intelligence. You can already feel the stone in your hands.')
        print(Fore.WHITE + 'Being an ever optimistic person, you get a bit carried away and you fail to pay attention to your surroundings.')
        print(Fore.WHITE + 'If you were paying attention, you would have noticed the big giant hole that opened up in front of you. As it is, you have not noticed and you fall into the hole.')
        print(Fore.WHITE + 'Death comes almost instantly as your body is pierced by hundreds of thin and very pointy sticks. You never noticed it, but hey, at least you died optimistically.')
        print(Fore.RED + 'Game Over')
        exit()
print(Fore.WHITE + 'Suddenly the ground seems to open up and a horde of goblins comes charging towards you.')

print(Fore.RED + '`````` ,      ,')
print(Fore.RED + '     /(.-""-.)\ ')
print(Fore.RED + ' |\  \/      \/  /| ')
print(Fore.RED + ' | \ / =.  .= \ / | ')
print(Fore.RED + '  \( \   o\/o  / )/ ')
print(Fore.RED + '   \_,   /  \  _/  ')
print(Fore.RED + '     /   \__/   \    ')
print(Fore.RED + '     \ \__/\__/ /    ')
print(Fore.RED + '   ___\ \|--|/ /___  ')
print(Fore.RED + '  /`    \      /    `\ ')
print(Fore.RED + ' /        ----        \ ') 

input(Fore.YELLOW + 'Press R to fight ')
jinitiative = random.randint (1,20) - 2
jinitiative = int(jinitiative)
ginitiative = random.randint (1,2) + 2
ginitiative = int(ginitiative)
if jinitiative >= ginitiative:
    print(Fore.GREEN +'You swing your great axe with both hands towards the first goblin that gets in range.')
    goblinhp = 2 * (random.randint (1,6))
    goblinarmour = 15
    goblinattack = random.randint (1,20) + 4
    goblindamage = random.randint (1,6) + 2
    jurgenhp = 12
    jurgenarmour = 17
    jurgenattack = random.randint (1,20) + 5
    jurgendamage = random.randint (1,12) + 3
    while jurgenhp >= 0:
        jurgenhp = jurgenhp - goblindamage    
        if jurgenattack >= goblinarmour:
            jurgendamage = random.randint (1,12) + 3
            print(Fore.GREEN +'Jurgen hits the goblin for ' + str(jurgendamage) + '.')
            goblinhp = 2 * (random.randint (1,6))
            if jurgendamage >= goblinhp:
                print(Fore.GREEN +'Your great axe splits the goblin in half')
                print('Another goblin takes its place.')
            if jurgendamage < goblinhp:
                print(Fore.GREEN +'You hit the goblin, but it is not a lethal hit.')
                print('Your hit does ' + str(jurgendamage) + ' hit points damage.')
                print('The goblin has ' + str(goblinhp - jurgendamage) + ' hit points left.')
                print(Fore.RED +'The goblin recovers and stabs his scimitar towards you.')
                if goblinattack > jurgenarmour:
                    print(Fore.RED + 'The goblins scimitars slashes through your armour.')
                    print(Fore.RED + 'The goblin scimitar cuts you for ' + str(jurgenhp - goblindamage) + ' hit points.')
                    if jurgenhp <= 0:
                        print(Fore.RED + 'The scimitar cuts a major artery. Blood sprays out of you and you die blooding on the ground.')
                        print(Fore.RED + 'Game over') 
                    if jurgenhp > 0:
                        print('The goblin wounded you but you are still able to fight.')
                if goblinattack <= jurgenarmour:
                    print('The scimitar harmlessly bounces off your armour.')   
            if goblindamage >= jurgenhp:
                    print(Fore.RED +'The goblins scimitar punches through your armour and you feel the blade piercing your heart')
                    print(Fore.RED +'While the blood squirts out of your heart, you feel your life flowing from you. There is only darkness now')
                    print(Fore.RED +'Game Over')
                    exit()
            if goblindamage < jurgenhp:
                    print(Fore.RED +'The goblin manages to cut you, fueling the rage you feel inside you. You ready your great axe for a swing')
                    jurgendamage = random.randint (1,12) + 3
                    print(Fore.GREEN +'Jurgen hits the goblin for ' + str(jurgendamage) + ' hit points.')
                    goblinhp = 2 * (random.randint (1,6))
                    if jurgendamage >= goblinhp:
                         print(Fore.GREEN +'Your great axe splits the goblin in half')
                         print(Fore.GREEN +'As the bloody remains splash to the ground, another goblin takes his place.')
                         print(Fore.GREEN +'You take a big swing with both arms.')
                         if goblinattack >= jurgenarmour:
                             print(Fore.RED +'The goblin manages to bypass your blocking move.')
                             print(Fore.RED +'You feel the scimitar punch through your armour')
                             goblindamage = random.randint (1,6) + 2
                             print(Fore.RED +'The goblin hits you and does ' + str(goblindamage) + 'points damage.')
                             print('You have ' + str(jurgenhp - goblindamage) + ' hit points left.')
                         if goblindamage >= jurgenhp:
                                 print(Fore.RED +'The goblins scimitar punches through your armour and you feel the blade piercing your heart')
                                 print(Fore.RED +'While the blood squirts out of your heart, you feel your life flowing from you. There is only darkness now')
                                 print(Fore.RED +'Game Over')
                                 exit()
        if jurgenattack < goblinarmour:
            print(Fore.GREEN +'Your greataxe hits the goblin, but it bounces off a piece of metal on the leather armour of the goblin')
            print(Fore.RED +'The goblin immediately reponds and swings it scimitar towards you')
            goblinattack = random.randint (1,20) + 4
            goblindamage = random.randint (1,6) + 2
            jurgenhp = 12
            jurgenarmour = 17
            jurgenattack = random.randint (1,20) + 5
            jurgendamage = random.randint (1,12) + 3
            if goblinattack >= jurgenarmour:
                print(Fore.RED +'The goblin manages to bypass your blocking move.')
                print(Fore.RED +'You feel the scimitar punch through your armour')
                goblindamage = random.randint (1,6) + 2
                if goblindamage >= jurgenhp:
                    print(Fore.RED +'The goblins scimitar punches through your armour and you feel the blade piercing your heart')
                    print(Fore.RED +'While the blood squirts out of your heart, you feel your life flowing from you. There is only darkness now')
                    print(Fore.RED +'Game Over')
                    exit()
                if goblindamage < jurgenhp:
                    print(Fore.RED+'The goblin does ' + str(goblindamage) + ' damage to you.')
                    print('You have ' + str(jurgenhp - goblindamage) + ' hit points left.')
                    print(Fore.RED +'The goblins hit fuels the rage you feel inside you. You ready your great axe for a swing.')
                    jurgendamage = random.randint (1,12) + 3
                    print(Fore.GREEN +'Jurgen hits the goblin for ' + str(jurgendamage) + ' hit points.')
                    goblinhp = 2 * (random.randint (1,6))
                    print(Fore.GREEN +'The goblin has ' + str(goblinhp - jurgendamage) + ' hit points left.')
                    if jurgendamage >= goblinhp:
                         print(Fore.GREEN +'Your great axe splits the goblin in half.')
                         print(Fore.GREEN +'As the bloody remains splash to the ground, another goblin takes his place.')
                         print(Fore.GREEN +'You take a big swing with both arms.')
                         if goblinattack >= jurgenarmour:
                             print(Fore.RED +'The goblin manages to bypass your blocking move.')
                             print(Fore.RED +'You feel the scimitar punch through your armour')
                             goblindamage = random.randint (1,6) + 2
                             print(Fore.RED +'The goblin hits you ' + str(goblindamage) + ' hit points.')
                             print('Jurgen has ' + str(jurgenhp - goblindamage) + ' hit points left.')
                                                    
                         if goblindamage >= jurgenhp:
                                 print(Fore.RED +'The goblins scimitar punches through your armour and you feel the blade piercing your heart')
                                 print(Fore.RED +'While the blood squirts out of your heart, you feel your life flowing from you. There is only darkness now')
                                 print(Fore.RED +'Game Over')
                                 exit()
            if goblinattack < jurgenarmour:
                print('Your armour protects you against the swing and the scimitar bounces off your armour.')
                print('You ready your axe to give the goblin a taste of your wraith.')
if jinitiative >= ginitiative:
    print(Fore.GREEN +'The goblin is fast as lighting and before you can block he makes a swing at you.')
    goblinhp = 2 * (random.randint (1,6))
    goblinarmour = 15
    goblinattack = random.randint (1,20) + 4
    goblindamage = random.randint (1,6) + 2
    jurgenhp = 12
    jurgenarmour = 17
    jurgenattack = random.randint (1,20) + 5
    jurgendamage = random.randint (1,12) + 3 
    while jurgenhp > 0:
        jurgenhp = jurgenhp - goblindamage
    if goblinattack >= jurgenarmour:
                print(Fore.RED +'The goblin manages to bypass your blocking move.')
                print(Fore.RED +'You feel the scimitar punch through your armour')
                goblindamage = random.randint (1,6) + 2
                if goblindamage >= jurgenhp:
                    print(Fore.RED +'The goblins scimitar punches through your armour and you feel the blade piercing your heart')
                    print(Fore.RED +'While the blood squirts out of your heart, you feel your life flowing from you. There is only darkness now')
                    print(Fore.RED +'Game Over')
                    exit()
                if goblindamage < jurgenhp:
                    print(Fore.RED+'The goblin does ' + str(goblindamage) + ' damage to you.')
                    print('You have ' + str(jurgenhp - goblindamage) + ' hit points left.')
                    print(Fore.RED +'The goblins hit fuels the rage you feel inside you. You ready your great axe for a swing.')
                    jurgendamage = random.randint (1,12) + 3
                    print(Fore.GREEN +'Jurgen hits the goblin for ' + str(jurgendamage) + ' hit points.')
                    goblinhp = 2 * (random.randint (1,6))
                    print(Fore.GREEN +'The goblin has ' + str(goblinhp - jurgendamage) + ' hit points left.')
                    if jurgendamage >= goblinhp:
                         print(Fore.GREEN +'Your great axe splits the goblin in half.')
                         print(Fore.GREEN +'As the bloody remains splash to the ground, another goblin takes his place.')
                         print(Fore.GREEN +'You take a big swing with both arms.')
                         if goblinattack >= jurgenarmour:
                             print(Fore.RED +'The goblin manages to bypass your blocking move.')
                             print(Fore.RED +'You feel the scimitar punch through your armour')
                             goblindamage = random.randint (1,6) + 2
                             print(Fore.RED +'The goblin hits you ' + str(goblindamage) + ' hit points.')
                             print('Jurgen has ' + str(jurgenhp - goblindamage) + ' hit points left.')
                                                    
                         if goblindamage >= jurgenhp:
                                 print(Fore.RED +'The goblins scimitar punches through your armour and you feel the blade piercing your heart')
                                 print(Fore.RED +'While the blood squirts out of your heart, you feel your life flowing from you. There is only darkness now')
                                 print(Fore.RED +'Game Over')
                                 exit()
    if goblinattack < jurgenarmour:
        print('Your armour protects you against the swing and the scimitar bounces off your armour.')
        print('You ready your axe to give the goblin a taste of your wraith.')