import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

lower = False
upper = False
numeric = False
for character in password:
    if len(password) < 6:
        break
    if len(password) > 16:
        break
    if character.islower():
        lower = True
    if character.isupper():
        upper = True
    if character.isnumeric():
        numeric = True


if lower==True and upper==True and numeric==True:
    is_valid=True
    
print(is_valid)
