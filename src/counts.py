import sys

x = (sys.stdin.read() if len(sys.argv) < 2 else sys.argv[1])
x = x.strip()

count = {}
for character in x:
    if character not in count:
        count[character] = 0
    count[character] += 1

for a in sorted(count):
    print(f"{a}: {count[a]}")


