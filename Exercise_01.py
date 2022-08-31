#list_01 = int(input('Input numbers'))
list_02 = [1,1,2,2,3,3,4,5,6,7,8,8]


def get_unique_list(n_list):
    new_list = []
    for c in n_list:
        if c not in new_list:
            new_list.append(c)
    
    return new_list

unique_list = get_unique_list(list_02)

print(unique_list)

