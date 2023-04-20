# number = 0
# while (number < 5):
#     number = number +1
#     print(number)

# print("done")
my_range = range(2,6)
print(my_range)


for x in my_range:
    print(x)
print("-----------------------------")

fun_fruits = ["melon", "banaana", "mango", "apple"]

for f in fun_fruits:
    print(f)
    for c in f:
        print(c)


print("-----------------------------")

foods = ["banana", "coffee", "honey"]
print(foods)
print (foods[2])


for food in foods:
    print(food)


print("-----------------------------")

for pet in ["dog", "cat", "bird"]:
    print ("give me a", pet)

print("-----------------------------")

for char in "coffee":
    print(char)