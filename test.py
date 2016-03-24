from variant import from_fact, to_sum
from math import exp

t = 1
u = 1
l = 5
n = 2
k = 1
a = from_fact(t, 2) + to_sum(t + 1, u + t)
b = from_fact(l - t - n - u + k, 2) + to_sum(l -
                                             t - n - u + k + 1, l - t - n - 1 + k)
print b
print exp(b)
