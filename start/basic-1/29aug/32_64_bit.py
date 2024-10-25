import struct, platform
bit = struct.calcsize("P") * 8
bit_num = platform.architecture()[0]
print(bit, bit_num)