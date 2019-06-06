
game = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


#print(game)

def gameboard():
    for row in game:
        print(row)



def plotting():
    for row in game:
        print(row)
    print("Please type the position you want to place on")

plotting()

input1 = int(input())

#Row one if else
if input1 == 1:
    game[0][0] = 'X'
elif input1 == 2:
    game[0][1] = 'X'
elif input1 == 3:
     game[0][2] = 'X'

#row two
elif input1 == 4:
    game[1][0] = 'X'
elif input1 == 5:
    game[1][1] = 'X'
elif input1 == 6:
     game[1][2] = 'X'
#row three
elif input1 == 7:
    game[2][0] = 'X'
elif input1 == 8:
    game[2][1] = 'X'
elif input1 == 9:
     game[2][2] = 'X'

gameboard()

input2 = int(input())
print("Please type the position the second player wants to play on")

if input2 == 1:
    game[0][0] = 'Y'
elif input2 == 2:
    game[0][1] = 'Y'
elif input2 == 3:
     game[0][2] = 'Y'


elif input2 == 4:
    game[1][0] = 'Y'
elif input2 == 5:
    game[1][1] = 'Y'
elif input2 == 6:
     game[1][2] = 'Y'

elif input2 == 7:
    game[2][0] = 'Y'
elif input2 == 8:
    game[2][1] = 'Y'
elif input2 == 9:
     game[2][2] = 'Y'

gameboard()

input1 = int(input())

print("Please type the position the first player wants to play on")
if input1 == 1:
    game[0][0] = 'X'
elif input1 == 2:
    game[0][1] = 'X'
elif input1 == 3:
     game[0][2] = 'X'


elif input1 == 4:
    game[1][0] = 'X'
elif input1 == 5:
    game[1][1] = 'X'
elif input1 == 6:
     game[1][2] = 'X'

elif input1 == 7:
    game[2][0] = 'X'
elif input1 == 8:
    game[2][1] = 'X'
elif input1 == 9:
     game[2][2] = 'X'




gameboard()

input2 = int(input())
print("Please type the position the second player wants to play on")

if input2 == 1:
    game[0][0] = 'Y'
elif input2 == 2:
    game[0][1] = 'Y'
elif input2 == 3:
     game[0][2] = 'Y'


elif input2 == 4:
    game[1][0] = 'Y'
elif input2 == 5:
    game[1][1] = 'Y'
elif input2 == 6:
     game[1][2] = 'Y'

elif input2 == 7:
    game[2][0] = 'Y'
elif input2 == 8:
    game[2][1] = 'Y'
elif input2 == 9:
     game[2][2] = 'Y'



gameboard()

input1 = int(input())

print("Please type the position the first player wants to play on")
if input1 == 1:
    game[0][0] = 'X'
elif input1 == 2:
    game[0][1] = 'X'
elif input1 == 3:
     game[0][2] = 'X'


elif input1 == 4:
    game[1][0] = 'X'
elif input1 == 5:
    game[1][1] = 'X'
elif input1 == 6:
     game[1][2] = 'X'

elif input1 == 7:
    game[2][0] = 'X'
elif input1 == 8:
    game[2][1] = 'X'
elif input1 == 9:
     game[2][2] = 'X'




gameboard()

input2 = int(input())
print("Please type the position the second player wants to play on")

if input2 == 1:
    game[0][0] = 'Y'
elif input2 == 2:
    game[0][1] = 'Y'
elif input2 == 3:
     game[0][2] = 'Y'


elif input2 == 4:
    game[1][0] = 'Y'
elif input2 == 5:
    game[1][1] = 'Y'
elif input2 == 6:
     game[1][2] = 'Y'

elif input2 == 7:
    game[2][0] = 'Y'
elif input2 == 8:
    game[2][1] = 'Y'
elif input2 == 9:
     game[2][2] = 'Y'



gameboard()



if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
    print("Strike!!")

elif game[0][0] == 'Y' and game[1][1] == 'Y' and game[2][2] == 'Y':
    print("Strike ")
