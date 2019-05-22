given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0

for i in given_list:
    if i < 0:
        total = i + total
print(total)



total = 0
print(list(range(100)))

for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
print(total)



def string_multiplication(s, ni):
    print(s * ni)

string_multiplication( "Hi", 2)



def Greet(name):
    print("Hey! Wassup?" + name)

Greet("Bob")


a = [2, 3, 9]
max_len = len(a)

for i in a:
    if a[0] == 6:
        print("True")
    elif a[max_len - 1] == 6:
        print("True")
    else:
        print("False")
    break








