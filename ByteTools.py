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
