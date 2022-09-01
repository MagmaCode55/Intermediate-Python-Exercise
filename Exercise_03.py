inp_01 = input('Enter String: ')


def num_elements(inp):
    dict_01 = {}
    inp_01 = inp.replace(" ", "")
    for i in inp_01:
        if i not in dict_01.keys():
            dict_01[i] = inp.count(i) 
    return dict_01

ans = num_elements(inp_01)
print(ans)