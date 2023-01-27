def min_terms_needed(g, x, max_error):
    tot = 0
    for k in range(1, 100000):
        cur = g(x, k)
        if abs(cur) < max_error:
            return k-1
        tot += cur
    return -1
