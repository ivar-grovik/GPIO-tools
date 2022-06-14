def mustBeMember(value, set):
    isMember = False
    for item in set:
        if item == value:
            isMember = True

    if not isMember:

        raise ValueError('Value ' + str(value) + ' must be part of set ', str(set))
