import sys

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command = sys.argv[1]
x = sys.argv[2]

encode_list = []
if command == 'encode':
    for character in x:
        encode_list.append(hex(ord(character)))
    print(''.join(encode_list))

decode_list = []
if command == 'decode':
    for num in x.split('0x')[1:]:
        decode_list.append(chr(int(num, base=16)))
    print(''.join(decode_list))


