import validation


def bin2int(bin_list, byte_size):
    combined = ""
    for number in bin_list:
        number = number[2:]
        if len(number) != byte_size:
            for j in range(0, byte_size - len(number)):
                number = "0" + number
        combined += number

    return int(combined, 2)


def combineBytes(byte_list, byte_size):
    validation.mustBeType(byte_list, "str")
    thresholds = []
    for i in range(1, len(byte_list)):
        thresholds.append(i * byte_size)

    if len(byte_list) == 2:
        combined = (byte_list[1] << thresholds[0]) | byte_list[0]
    elif len(byte_list) == 3:
        combined = (byte_list[2] << thresholds[1]) | (byte_list[1] << thresholds[0]) | (byte_list[0])

    return bin(combined)


def changeBit(old_byte, new_bits, bit_ind):
    validation.mustBeSameLength(new_bits, bit_ind)
    if isinstance(new_bits, int):
        new_bits = bin(new_bits)
    if isinstance(old_byte, int):
        old_byte = bin(old_byte)
    old_byte = old_byte[::-1]
    for i in range(0, len(old_byte)):
        for j in range(0, len(bit_ind)):
            if bit_ind[j] == i:
                old_byte = old_byte[:i] + str(new_bits[j]) + old_byte[i+1:]

    return old_byte[::-1]

def bin2List(binary):
    output = []
    if isinstance(binary, int):
        binary = bin(binary)
    for i in range(2, len(binary)):
        output.append(int((binary[i])))

    return output

    return temp

def to8Bit(num):
    if isinstance(num, str):
        num = int(num, 2)
    bit = f'{num:08b}'
    bit = "0b"+bit
    return bit

def getBits(num, bit_ind):
    prefix = "0b"
    output = ""
    if isinstance(num, int):
        num = bin(num)
    num = num[::-1]
    for i in range(0, len(num)-2):
        for j in bit_ind:
            if j == i:
                output += num[i]
    output = output[::-1]

    return prefix + output

def to3Bit(num):
    if isinstance(num, str):
        num = int(num, 2)
    bit = f'{num:03b}'
    bit = "0b"+bit
    return bit


def str2int(values):
    if isinstance(values, list):
        converted = []
        for value in values:
            if '0b' in value[:2]:
                base = 2
            elif '0x' in value[:2]:
                base = 0
            else:
                raise ValueError(value)
            converted.append(int(value, base))
    else:
        if '0b' in values[:2]:
            base = 2
        elif '0x' in values[:2]:
            base = 0
        else:
            raise ValueError(values)
        converted = int(values, base)

    return converted
