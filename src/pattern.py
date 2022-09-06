counts = 0
pattern = ''
for j in range(1,10,1):
    if j <= 5:
        counts += 1
        pattern = '* ' * counts
    if j > 5:
        counts -= 1
        pattern = '* ' * counts
    print(pattern.strip())
