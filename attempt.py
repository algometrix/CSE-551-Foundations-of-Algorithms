


def solve(arr, com_tracker=[], j = 0):
    print(arr)
    arr_length = len(arr)
    
    if arr_length == 2:
        if arr[0] > arr[1]:
            return 0, []
        else:
            return 1, []

    half_length = int(arr_length/2)
    sort_track = [ 0 ] * half_length
    swap_track = [ 0 ] * half_length

    if com_tracker != None:
        pass
    
    for i in range(0, half_length):
        if arr[2*i] > arr[2*i + 1]:
            sort_track[i] = 2*i
            swap_track[i] = 0
        else:
            sort_track[i] = 2*i + 1
            swap_track[i] = 1

    new_list = [ arr[i] for i in sort_track  ]
    rec_call,s = solve(new_list, j = j+1)
    print(s)
    rec_call = 2*rec_call + swap_track[rec_call]
    return rec_call, [sort_track,s]

if __name__ == '__main__':
    arr = [9,2,1,3, 5,7,1,8]
    index,s = solve(arr)
    print("Max Value at Index : {}".format(index))
    print(s)
    arr[index] = 6
    index,s = solve(arr)
    print("\nMax Value at Index : {}".format(index))
    print(s)
