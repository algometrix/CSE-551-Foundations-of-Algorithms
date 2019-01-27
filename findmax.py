from itertools import permutations 

num_list = [1,2,3,9,9,6,]

def find_max(arg_list):
    length = len(arg_list)
    j = length - 1
    k = length - 2
    m = arg_list[length - 1]
    update_count = 0
    while(k>=0):
        if arg_list[k] <= m:
            k = k - 1
        else:
            j = k
            m = arg_list[k]
            update_count += 1
            k = k - 1
    
    return m, update_count

def findsubsets(num):
    l = list(permutations(range(1, num + 1))) 
    return l

#print(find_max([2,1]))

calc_range = 6
for i in range(1,calc_range):
    values = findsubsets(i)
    max_values = [0] * calc_range
    update_values = [0] * calc_range
    permuations = [0] * calc_range
    for num_list in values:
        print(num_list)
        maximum_val, update_counter = find_max(num_list)
        update_values[i] += update_counter
        permuations[i] += 1
        
    print('Max : {} and Updates : {} and Permuations : {}'.format(maximum_val, update_values[i], permuations[i]))