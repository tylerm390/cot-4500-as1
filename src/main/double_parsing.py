def parse_double(bin_string, rnd):
    zeros = "0" * (64 - len(bin_string))
    bin_string += zeros
    sign = int(bin_string[0], 2)
    exponent = int(bin_string[1:12], 2)
    mantissa = 0
    half_pow = 1 / 2
    for i in range(12, 64):
        mantissa += half_pow * (bin_string[i] == '1')
        half_pow /= 2
        
    return rnd((-1) ** sign * (2 ** (exponent - 1023)) * (1 + mantissa))
