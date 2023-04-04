class Function:
    """
    Wrap a function from a domain onto itself that is
    both onto and one-to-one (i.e. bijective).
    """
    def __init__(self, domain, f):
        self.domain = domain
        self.f = f
        assert set(f(x) for x in domain) == domain

    def __eq__(self, other):
        assert self.domain == other.domain
        return all(self.f(elem) == other.f(elem) for elem in self.domain)

    def __mul__(self, other):
        # Define multiplication as function composition!
        return Function(self.domain, lambda x: other.f(self.f(x)))

    def __call__(self, n):
        assert n in self.domain
        return self.f(n)

domain = {0, 1, 2}

add0 = Function(domain, lambda x: (0 + x) % 3)
add1 = Function(domain, lambda x: (1 + x) % 3)
add2 = Function(domain, lambda x: (2 + x) % 3)

assert add0 * add0 == add0
assert add0 * add1 == add1
assert add0 * add2 == add2
assert add1 * add1 == add2
assert add1 * add2 == add0
assert add2 * add2 == add1

assert (add2 * add2)(1) == 2

import group

group.verify_group_properties(
    members=[add0, add1, add2],
    identity=add0,
)


def permutor(lst):
    def f(elem):
        return lst[elem]

    return f


rot0 = permutor([0, 1, 2])
rot1 = permutor([1, 2, 0])
rot2 = permutor([2, 0, 1])

assert rot1(rot1(0)) == 2 == rot2(0)

rotate0 = Function(domain, rot0)
rotate1 = Function(domain, rot1)
rotate2 = Function(domain, rot2)

group.verify_group_properties(
    members=[rotate0, rotate1, rotate2],
    identity=rotate0,
)

assert Function(domain, rotate0) == Function(domain, add0)
assert Function(domain, rotate1) == Function(domain, add1)
assert Function(domain, rotate2) == Function(domain, add2)

fix0 = Function(domain, permutor([0, 2, 1]))
fix1 = Function(domain, permutor([2, 1, 0]))
fix2 = Function(domain, permutor([1, 0, 2]))


group.verify_group_properties(
    members=[rotate0, rotate1, rotate2, fix0, fix1, fix2],
    identity=rotate0,
)

group.verify_group_properties(
    members=[rotate0, fix0],
    identity=rotate0,
)

group.verify_group_properties(
    members=[rotate0, fix1],
    identity=rotate0,
)

group.verify_group_properties(
    members=[rotate0, fix2],
    identity=rotate0,
)

r0 = rotate0
r1 = rotate1
r2 = rotate2
f0 = fix0
f1 = fix1
f2 = fix2

multiplication_table = [
    [r0, r1, r2, f0, f1, f2],
    [r1, r2, r0, f1, f2, f0],
    [r2, r0, r1, f2, f0, f1],
    [f0, f2, f1, r0, r2, r1],
    [f1, f0, f2, r1, r0, r2],
    [f2, f1, f0, r2, r1, r0],
]

for i, x in enumerate([r0, r1, r2, f0, f1, f2]):
    for j, y in enumerate([r0, r1, r2, f0, f1, f2]):
        assert x * y == multiplication_table[i][j]
