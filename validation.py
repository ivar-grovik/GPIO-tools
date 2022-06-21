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

def mustBeSameLength(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError("Lists ", list_1, " and ", list_2, " must be same length")