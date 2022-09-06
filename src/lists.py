import sys


x = sys.stdin.read()
x = x.strip().split(' ')


def print_list(x):
    print(" ".join(str(i) for i in x))
    return ''

if len(sys.argv) < 2:
    print("Incorrect number of arguments.", file=sys.stderr)
    sys.exit(1)

# mean:
if sys.argv[1] == 'mean':
    x_sum = 0
    for j in x:
        x_sum+=int(j)
    mean = x_sum/len(x)
    print(mean)

# times three:
times_three = []
for j in x:
    times_three.append(int(j)*3)
print_list(times_three)


# even:
even = []
for j in x:
    if int(j) % 2 == 0:
        even.append(j)
print_list(even)


print('input list: ', x)