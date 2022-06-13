def bin2int(bin_list, byte_size):
    combined = ""
    for number in bin_list:
        number = number[2:]
        print(number)
        if len(number) != byte_size:
            for j in range(0, byte_size - len(number)):
                number = "0" + number
        combined += number

    return int(combined, 2)