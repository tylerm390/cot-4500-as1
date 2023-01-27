def bisection(f, lo, hi, eps):
    max_itr = 100000
    for itr in range(0, max_itr):
        md = (lo + hi) / 2
        if abs(lo - hi) < eps:
            return (md, itr)
        if (f(lo) < 0 and f(md) > 0) or (f(lo) > 0 and f(md) < 0):
            hi = md
        else:
            lo = md
    return (-1, -1)

def newton_raphson(f, df, x0, eps):
    max_itr = 100000
    x = x0
    for itr in range(1, max_itr + 1):
        diff = f(x) / df(x)
        if abs(diff) < eps:
            return (x, itr)
        x -= diff
    return (-1, -1)
