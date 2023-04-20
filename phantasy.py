import random

luck = random.randint(1,3)
strength = random.randint(3,15)
magic = random.randint(3,15)
health = random.randint(3,15)
initiative = random.randint(3,15)
msg= ""
print("Welcome to phantasy")
players = int(input("How many players?"))

player_names=[]
i = 0
while (i < players):
    name = input("enter players name: ")
    player_names.append(name)

    
    if luck == 1:
        # barbarian
        msg = msg + "\n" + player_names[i] + " is a Barbarian"
        strength = strength * 3
        health = health *3
        

    elif luck == 2:
        # Cleric
        msg = msg + "\n" +  player_names[i]+ " is a Cleric"
        magic = magic * 3
        initiative = initiative * 3
    else:
        # Druid
        msg = msg + "\n" + player_names[i] + " is a Druid"
        health = health *2
        magic = magic * 2
        initiative = initiative * 2  

    msg = msg + "\n-> Strength:  " + str(strength) + "\n-> Magic:  " +str(magic) + "\n-> Health:  + "+ str(health) +" \n-> Initiative:  "+ str(initiative)
   
    i = i+1

print(msg)
 





