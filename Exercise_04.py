list_01 = []
counter = 1
while len(list_01) !=  5:
    
    try:
        
        inp_01 = int(input(f"Enter int #{counter}: "))
        list_01.append(inp_01)
        counter+=1
    except ValueError as er:
        print('Invalid input. Please enter an int')

print(list_01)