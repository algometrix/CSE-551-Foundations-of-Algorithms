

def find_peak(numbers):
    length = len(numbers)
    if length == 2:
        return max(numbers)
    if length == 1:
        return numbers[0]
    half = int(length/2)
    half_way = numbers[half]
    before_half_way = numbers[half - 1]
    after_half_way = numbers[half + 1]
    if before_half_way < half_way and half_way < after_half_way:
        return find_peak(numbers[half:])
    elif before_half_way > half_way and half_way > after_half_way:
        return find_peak(numbers[:half])
    elif before_half_way < half_way and half_way > after_half_way:
        return half_way

if __name__ == '__main__':
    input_list = [10,9,8]
    peak_val = find_peak(input_list)
    print('Peak Value : {}'.format(peak_val))