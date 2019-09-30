import random
import time as t


random_number = random.randint(0, 100)
no_guesses = 0


main_list = []

for i in range(101):
    main_list.append(i)


random_key = "02827234"

print("press any key to start!!")
press_start = int(input())
if press_start != random_key:
    pass

print("Bringing Number guessing game... ")
t.sleep(1.5)
print("I have choosen a number between 1 and 100 try to guess that number")
print("If you are an admin press 1 else type any other key and press enter")
admin = int(input())
if admin == 1:
    print(random_number)
else:
    print("You can continue with the game")
a = 0

def logic_guess1():
    if guess == random_number:
        print("You got it right!! you only took 1 guess")

guess = int(input())

def logic():
    guess = int(input())
    if guess == random_number:
        print("Congrats you only took ", a + 1, "guesses")
    elif guess < random_number:
        print("The guessed number is smaller than the choosen number")
    elif guess > random_number:
        print("The guessed number is greater than the choosen number ")

while guess != random_number or guess == random_number:
    a += 1
    if guess == random_number:
        print("Congrats you got it right", "you only took 1 guess")
        break
    elif guess < random_number:
        print("The guessed number is smaller than the choosen number")
        while guess != random_number:
            logic()
            if guess == random_number:
                 break
            a = a + 1
    elif guess > random_number:
        print("The guessed number is greater than the choosen number")
        while guess != random_number:
            logic()
            if guess == random_number:
                 break
            a += 1

