
def find_share_profit(share_prices):
    length = len(share_prices)
    half = int(length/2)
    if length == 2:
        return {'max': share_prices[1], 'min': share_prices[0]}
    else:
        fir_half = find_share_profit(share_prices[:half])
        sec_half = find_share_profit(share_prices[half:])
        fir_half_max = fir_half['max']
        fir_half_min = fir_half['min']
        sec_half_max = sec_half['max']
        sec_half_min = sec_half['min']
        share_max = max(fir_half_max, sec_half_max)
        #print('array : {}'.format(share_prices))
        #print('share_max : {}'.format(share_max))
        share_min = min(fir_half_min, sec_half_min)
        #print('share_min : {}'.format(share_min))
        return {'max': share_max, 'min': share_min}


if __name__ == '__main__':
    prices = [90, 2, 3, 9, 11, 15, 1, 100]
    result = find_share_profit(prices)
    print(result)
