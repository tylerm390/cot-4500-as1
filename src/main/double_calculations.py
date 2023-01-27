def actual(a):
    return a

def truncate(a):
    pow10 = 1
    while a / pow10 > 10 ** 3:
        pow10 *= 10
    while a / pow10 < 1:
        pow10 /= 10
    return int(a / pow10) * pow10

def rounding(a):
    pow10 = 1
    while a / pow10 > 10 ** 3:
        pow10 *= 10
    while a / pow10 < 1:
        pow10 /= 10
    return round(a / pow10) * pow10
