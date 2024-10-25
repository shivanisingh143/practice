import sys

print()
if sys.byteorder == 'little':
    print("little")
else:
    print("big endian")
print()
