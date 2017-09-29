def cube(x): return x*x*x

print map(cube, range(1, 5))


def f(x): return x % 3 == 0 or x % 5 == 0
print filter(f, range(2,25))

