#list_01 = int(input('Input numbers'))
list_02 = [1,1,2,2,3,3,4,5,6,7,8,8]


def get_unique_list(n_list):
    new_list = []
    for c in n_list:
        if n_list.count(c) == 1:
            new_list.append(c)
    
    print(new_list)
