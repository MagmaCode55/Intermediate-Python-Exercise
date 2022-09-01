inp_01 = input('Enter String: ')


def num_elements(inp):
    dict_01 = {}
    for i in inp:
        if i not in dict_01.keys():
            dict_01[i] = inp.count(i) 
    return dict_01