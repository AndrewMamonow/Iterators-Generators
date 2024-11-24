def flat_generator(list_of_list):
    for sub_list in list_of_list:
        for element in sub_list:
            yield element

def flat_generator_2(list_of_list):
    for sub_list in list_of_list:
        if isinstance(sub_list, list):
            for element in flat_generator_2(sub_list):
                yield element
        else:
            yield sub_list
