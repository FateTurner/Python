given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0

for i in given_list:
    if i < 0:
        total = i + total
print(total)

