## The simulation of CPU
'''

只有两个输入都是1的时候，输出0，否则就输出1

'''

def nand(a, b): return 0 if a == b == 1 else 1

def not_(in_):
    return nand(in_, in_)

def and_(a, b): 
    return not_(nand(a, b))


def or_(a, b):
    return not_(
        and_(
            not_(a), not_(b)
        )
    )


def xor_(a, b):
    aOrb = or_(a, b)
    aAndb = and_(a, b)
    notAnd = not_(aAndb)
    return and_(notAnd, aOrb)

def mux(a, b, sel):
    nots = not_(sel)
    notsOrb = or_(nots, b)
    aAndNotSorB = and_(a, notsOrb)
    notA = not_(a)
    notAandB = and_(notA, b)
    notAandBandS = and_(notAandB, sel)
    out = or_(aAndNotSorB, notAandBandS)

    return out


def dmux(in_, sel):
    notSel = not_(sel)
    a = and_(in_,notSel)
    b = and_(in_, sel)

    return a, b

## Next Step:  Mathmactical Opeartion

def add(a, b): # half-add
    return xor_(a, b), and_(a, b)

def full_add(a, b, c):
    a_b_sum, a_b_carray = add(a, b)
    sum_, carray_c = add(a_b_sum, c)
    carry, _ = add(carray_c, a_b_carray)

    return sum_, carry

def add16(a, b):
    out = [None] * 16

    out[-1], c1 = full_add(a[-1], b=b[-1], c=0)
    out[-2], c2 = full_add(a[-2], b=b[-2], c=c1)
    out[-3], c3 = full_add(a[-3], b=b[-3], c=c2)
    out[-4], c4 = full_add(a[-4], b=b[-4], c=c3)
    out[-5], c5 = full_add(a[-5], b=b[-5], c=c4)
    out[-6], c6 = full_add(a[-6], b=b[-6], c=c5)
    out[-7], c7 = full_add(a[-7], b=b[-7], c=c6)
    out[-8], c8 = full_add(a[-8], b=b[-8], c=c7)
    out[-9], c9 = full_add(a[-9], b=b[-9], c=c8)
    out[-10], c10 = full_add(a[-10], b=b[-10], c=c9)
    out[-11], c11 = full_add(a[-11], b=b[-11], c=c10)
    out[-12], c12 = full_add(a[-12], b=b[-12], c=c11)
    out[-13], c13 = full_add(a[-13], b=b[-13], c=c12)
    out[-14], c14 = full_add(a[-14], b=b[-14], c=c13)
    out[-15], c15 = full_add(a[-15], b=b[-15], c=c14)
    out[-16], c16 = full_add(a[-16], b=b[-16], c=c15)

    return out

assert nand(0, 0) == 1
assert nand(1, 0) == 1
assert nand(1, 1) == 0
assert nand(0, 1) == 1

assert not_(0) == 1
assert not_(1) == 0

assert and_(0, 0) == 0
assert and_(1, 0) == 0
assert and_(0, 1) == 0
assert and_(1, 1) == 1

assert or_(0, 0) == 0
assert or_(1, 0) == 1
assert or_(0, 1) == 1
assert or_(1, 1) == 1


assert xor_(0, 0) == 0
assert xor_(1, 1) == 0
assert xor_(1, 0) == 1
assert xor_(0, 1) == 1

assert mux(a=0, b=0, sel=0) == 0
assert mux(a=1, b=0, sel=0) == 1
assert mux(a=0, b=1, sel=0) == 0
assert mux(a=1, b=1, sel=0) == 1
assert mux(a=0, b=0, sel=1) == 0
assert mux(a=1, b=0, sel=1) == 0
assert mux(a=0, b=1, sel=1) == 1
assert mux(a=1, b=1, sel=1) == 1

assert dmux(0, 0) == (0, 0)
assert dmux(1, 0) == (1, 0)
assert dmux(0, 1) == (0, 0)
assert dmux(1, 1) == (0, 1)

assert add(0, 0) == (0 , 0)
assert add(1, 0) == (1 , 0)
assert add(0, 1) == (1 , 0)
assert add(1, 1) == (0 , 1)


full_add_test_cases = [
    (0, 0, 0, 0, 0),
    (0, 0, 1, 1, 0),
    (0, 1, 0, 1, 0),
    (0, 1, 1, 0, 1),
    (1, 0, 0, 1, 0),
    (1, 0, 1, 0, 1),
    (1, 1, 0, 0, 1),
    (1, 1, 1, 1, 1),
]

for args in full_add_test_cases:
    assert full_add(*args[:3]) == args[-2:]


print('test done!')

if __name__ == '__main__':
    num1 = '0000000000000001' # 1
    num2 = '0000000000000111' # 7
    
    def s2b(string): return list(map(int, string))

    num3 = '0001111111111100' # 8188
    num4 = '0000000000000111' # 7

    print(add16(s2b(num3), s2b(num4)))

    num4 = '1111111111111111' # 131071
    num5 = '0000000000000111' # 7

    print(add16(s2b(num4), s2b(num5)))



    
