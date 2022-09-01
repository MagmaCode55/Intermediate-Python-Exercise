my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

def get_combined_dict(dict_01, dict_02):
    final_dict = {}
    for i in dict_01.keys():
        for j in dict_02.keys():
            if(i == j):
                fin_dict[i] = (dict_01[i]+dict_02[j])

    return final_dict

combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
