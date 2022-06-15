def mustBeMember(value, set):
    isMember = False
    for item in set:
        if item == value:
            isMember = True

    if not isMember:

        raise ValueError('Value ' + str(value) + ' must be part of set ', str(set))

def mustBeType(value, obj_type):
    bad_type = False
    for item in value:
        if type(item) == obj_type:
            bad_type = True

    if bad_type:
        raise ValueError('Value(s)' + str(value) + ' must be of type ', str(obj_type))