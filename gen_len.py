#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from itertools import izip
from random import randint, sample
from collections import Counter

import variant

def variant_count(l, L, N):
    res = 0.0
    for k in xrange(1, N):
        res += variant.p_line(k, L, N, l)
    return res

def main():
    L = 4
    N = 2

    N_ITER = 10**5

    lengths = Counter()
    counts = 0

    choices = range(0, L)
    length_counter = Counter()

    for _ in xrange(N_ITER):
        rand_vec = sample(choices, N)
        rand_vec.sort()
        for l in ((c - b) for (b, c) in izip(rand_vec, rand_vec[1:])):
            if l == 0:
                continue
            counts += 1
            length_counter[l] += 1

    for (l, count) in length_counter.items():
        res = variant_count(l, L, N)/(N-1)
        print "%d\t%f\t%f" % (l, float(count) / counts, res)

if __name__ == "__main__":
    main()
