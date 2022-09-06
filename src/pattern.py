counts = 0
for j in range(1,10,1):
    if j <= 5:
        counts += 1
    if j > 5:
        counts -= 1
    print('*' * counts)
