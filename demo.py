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