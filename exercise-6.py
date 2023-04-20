import random

# guess = input("please type in your guess: ")
# guess = int(guess)
# number = random.randint(0,10000)
# counter = 1
# while (guess != number):
    
   
#     if guess < number:
#         print("wrong answer- too small. this is your", counter, "try")
#         guess = input("please type your guess again: ")
#         guess = int(guess)
#         counter = counter +1
    
#     elif guess > number:
#         print("wrong answer- too large. this is your", counter, "try")
#         guess = input("please type your guess again: ")
#         guess = int(guess)
#         counter = counter +1
    
   
       

    
# print("correct answer!") 


# task 2 


first_num = 0
second_num = 1
for i in range(0,50):
    
    fibo_num = first_num + second_num
    print(fibo_num)
    first_num = second_num
    second_num = fibo_num


