import sys

x = sys.argv[1]

count = {}
for character in x:
    if character not in count:
        count[character] = 0
    count[character] += 1

for a in sorted(count):
    print(f"{a}: {count[a]}")
