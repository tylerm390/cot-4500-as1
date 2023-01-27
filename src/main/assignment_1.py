import double_parsing as parse
import double_calculations as calc
import error
import infinite_series as inf_ser
import root_finding as roots

actual = parse.parse_double("010000000111111010111001", calc.actual) 
print(actual, end='\r\n\r\n')

truncated = parse.parse_double("010000000111111010111001", calc.truncate)
print("{:.1f}".format(truncated), end='\r\n\r\n')

rounded = parse.parse_double("010000000111111010111001", calc.rounding)
print("{:.1f}".format(rounded), end='\r\n\r\n')

absolute_error = error.absolute(actual, rounded)
relative_error = error.relative(actual, rounded)
print(absolute_error, end='\r\n')
print("{:.31f}".format(relative_error), end='\r\n\r\n')

def g(x, k):
    return (-1)**k * ((x ** k) / (k ** 3))

print(inf_ser.min_terms_needed(g, 1, 1e-4), end='\r\n\r\n')

def f(x):
    return x**3 + 4 * x ** 2 - 10

def df(x):
    return 3 * x ** 2 + 8 * x

bs_ans, bs_itr = roots.bisection(f, -4, 7, 1e-4)
print(bs_itr, end='\r\n\r\n')

nr_ans, nr_itr = roots.newton_raphson(f, df, -4, 1e-4)
print(nr_itr, end='\r\n\r\n')
