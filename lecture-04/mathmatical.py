from basic_elements import *


def half_add(a, b):
    return xor_(a, b), and_(a, b)


def full_add(a, b, c):
    a_b_sum, a_b_carry = half_add(a, b)
    sum_, carry_c = half_add(a_b_sum, c)
    carry, _ = half_add(carry_c, a_b_carry)

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


def sub16(a, b):
    return add16(a, add16(not16(x), [0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0,0,0,0,1]))
    

assert half_add(0, 0) == (0, 0)
assert half_add(1, 0) == (1, 0)
assert half_add(0, 1) == (1, 0)
assert half_add(1, 1) == (0, 1)

assert full_add(0, 0, 0) == (0, 0)
assert full_add(0, 1, 0) == (1, 0)
assert full_add(0, 0, 1) == (1, 0)
assert full_add(1, 0, 0) == (1, 0)
assert full_add(1, 1, 0) == (0, 1)
assert full_add(1, 1, 1) == (1, 1)

print('test fininshed')

a = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(a, b, add16(a, b))

a = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
b = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
print(a, b, add16(a, b))

a = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
b = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
print(a, b, add16(a, b))

a = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1] # 17
b = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0] # 6
print(a, b, add16(a, b))


