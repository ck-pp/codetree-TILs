from math import pow

def bin_to_dec(binary):
    res = 0
    power = 0
    while binary > 0:
        res += (binary % 10) * pow(2, power)
        binary //= 10
        power += 1
    
    return int(res)

dec = bin_to_dec(int(input()))
print(bin(dec * 17)[2:])