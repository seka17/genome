b = 0
b1 = 0
b2 = 0
small_counter = Counter()
for _ in xrange(N_ITER):
    f1 = False
    f2 = False
    rand_vec = sample(choices, N)
    rand_vec.sort()
    # if rand_vec[0] == 0:
    #     f1 = True
    #     rand_vec = rand_vec[1:]
    # if rand_vec[-1] == L - 1:
    #     f2= True
    #     rand_vec = rand_vec[:-1]
    if not f1 and not f2:
        b += 1
    elif f1 and f2:
        b2 += 1
        # N_ITER +=1
        continue
    else:
        b1 += 1
    # rand_vec.extend([0, L - 1])
    rand_vec.extend([L - 1])
    rand_vec.sort()
    # print rand_vec
    for l in ((c - b) for (b, c) in izip(rand_vec, rand_vec[1:])):
        if l == 0:
            continue
        counts += 1
        small_counter[l] += 1

b, b1, b2 = map(lambda x: x / N_ITER, [b, b1, b2])
n, n1, n2 = map(lambda x: x / binom(N, L),
                [binom(N, L - 2), 2 * binom(N - 1, L - 2), binom(N - 2, L - 2)])
print b, b1, b2, n, n1, n2

print small_counter
t1 = 0
t2 = 0
for (l, count) in small_counter.items():
    # res = variant_count(l, L-1, N-1)*var*2  + variant_count(l, L, N)*(1.0-4*var)
    res1 = variant_count(l, L, N)  # для случая, когда нет фиксированных точек
    # для случая, когда есть одна фиксированная точка
    res2 = variant_count(l, L - 1, N)
    # для случая, когда есть две фиксированные точки
    res3 = variant_count(l, L - 2, N)
    border = (lambda x: binom(N - 1, L - l - 1) /
              binom(N, L - 1) if L - l - 1 >= N - 1 else 0)(1)
    border1 = (lambda x: binom(N - 1, L - l - 2) / binom(N, L - 2)
               if L - l - 2 >= 0 and L - l - 2 >= N - 1 else 0)(1)
    # try:
    #     border1 = binom(N-1, L-l-2)/binom(N, L-2)
    # except:
    #     border1 = 1/binom(N, L-2)
    f1 = lambda x: 1. / x if border != 0 else 0
    f2 = lambda x: 1. / x if border1 != 0 else 0
    # *binom(N,L-2)/(N-1) + (res2+2*border)*binom(N-1,L-2)*f1(N) + (res3+2*border1)*binom(N-2,L-2)*f2(N)
    res = res1 / (N - 1)
    # res /= binom(N,L)
    # print border1, border, f1(N), f2(N)
    # res = (res2+border)/(N)
    # print border
    # res = (variant_count(l,L-1,N)+border)/N
    # res /= binom(N,L)*(binom(N,L-2)*(N-1) + 2*binom(N-1,L-2)*N + binom(N-2,L-2)*(N+1))
    # res = res2
    # print "%d: var=%f\tvar_board1=%f\tvar_board2=%f\tres=%f" % (l, res1, res2, res3, res)
    # res =
    # res = 0
    # for k in xrange(1, N):
    #     if k==1:
    #         res += p_line(k, L-1, )
    #     r= p_line11(k, L, N, l)
    #     # r /= (N)
    #     # if k == 1:
    #     #     border_p = p_point(1, L, N-1, l)
    #     # #     odd1 = (1-border_p)*(odd*10**5)/10**5
    #     #     # r += 2.0*border_p / N
    #     # #     # r += (2*border_p - border_p ** 2)*odd
    #     res += r
    # res /= N-1
    # P + (1-P)*P = 2*P - P^2
    # res = float(res)/(float(N)/L+float(N-1)/L**2+float(L-N)*(L-N-1)/L/(L-1))
    # res = float(res) / (float(N**2) / L + float(N) * (N - 1)**2 /
    # L / (L - 1) + (L - N) * (L - N - 1) * (N + 1) / L / (L - 1))
    print "%d\t%f\t%f" % (l, float(count) / counts, res)
    t1 += float(count) / counts
    t2 += res
print(t1, t2)


def from_fact(x, power):
    res = 0
    if x >= big_number:
        # Приближенный результат
        res = x * (log(x) - 1)
    else:
        res = sum(map(lambda x: log(x), [v for v in xrange(1, x + 1)]))
    return power * res

def ln_binom(k, n):
    return ln_factorial(n) - (ln_factorial(k) + ln_factorial(n - k))

def ln_p_point(k, L, n, t):
    return ln_binom(k - 1, t) + ln_binom(n - k, (L - 1) - t) - ln_binom(n, L)

def binom(k, n):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def p_point(k, L, n, t):
    return binom(k - 1, t) * binom(n - k, (L - 1) - t) / binom(n, L)

def p_line(k, L, n, u):
    summary = 0.0
    tmin = k - 1
    tmax = L - (n - k) - u
    for t in xrange(tmin, tmax + 1):
        summary += p_point(k, L, n, t) * p_point(1,
                                                 L - (t + 1), n - k, u - 1)
    return summary
