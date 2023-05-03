def test_outer_f():
    s = 5
    def test_inner_f():
        nonlocal s
        s =  s+1
        return s
    return test_inner_f()

print(test_outer_f())