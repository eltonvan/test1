import random
print("welcome")

name1=(input("charachter1: "))
name2=(input("charachter1: "))
name3=(input("charachter1: "))
name4=(input("charachter1: "))
name5=(input("charachter1: "))

luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)


if luck == 1:
    # warrior
    print(name1 + " is a warrior")
    strength = strength * 3

elif luck == 2:
    # wizard
    print(name1 + " is a wizard")
    magic = magic * 3
else:
    # potato
    print(name1 + " is a potato")
    health = health *3

print ("-> Strength: ", strength)
print ("-> Magic: ", magic)
print ("-> Health: ", health)

