def verify_group_properties(members, identity):
    # verify distinctness, since we use Python lists
    # (we use Python lists since sets are hard to hash)
    for i in range(len(members)):
        for j in range(len(members)):
            if i != j:
                assert members[i] != members[j]
    # closure
    for a in members:
        for b in members:
            assert a * b in members

    # associativity
    for a in members:
        for b in members:
            for c in members:
                assert (a * b) * c == a * (b * c)

    # identity
    for a in members:
        assert (a * identity) == a
        assert (identity * a) == a

    # inverse
    for a in members:

        def is_inverse(b):
            return (b * a == identity) and (a * b == identity)

        assert any(is_inverse(b) for b in members)
