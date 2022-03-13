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