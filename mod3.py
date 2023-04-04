class Mod3:
    def __init__(self, n):
        assert n in [0, 1, 2]
        self.n = n

    def __eq__(self, other):
        return self.n == other.n

    def __add__(self, other):
        return Mod3((self.n + other.n) % 3)

    def __mul__(self, other):
        # Just use * as another name for +, for convenience
        return self + other


zero = Mod3(0)
one = Mod3(1)
two = Mod3(2)

assert zero + zero == zero
assert zero + one == one
assert zero + two == two
assert one + one == two
assert one + two == zero  # 1 + 2 - 3
assert two + two == one  # 2 + 2 - 3

multiplication_table = [
    [zero, one, two],
    [one, two, zero],
    [two, zero, one],
]

for i in [0, 1, 2]:
    for j in [0, 1, 2]:
        assert Mod3(i) * Mod3(j) == multiplication_table[i][j]

import group

# This group happens to be Abelian (i.e. commutative), but we will
# only verify that it's a group.

group.verify_group_properties(
    members=[zero, one, two],
    identity=zero,
)
