# AI engineers 

# => solve the problems that not be solved efficiently.
# => Computer Science foundamental & principle: CPU is the kernel of morden computer
# => CPU is the core capability between countries.
# => Quantum Computer, modern cpu

# CPU == Central Processing Unit
# ALU: 算数计算单元 RAM: 存储设备

# 半导体: 通电的话，当电压高过某个阈值的时候，这个器件可以成为导体
# 高于某个阈值的电：高电压，1， True
# 到电压低于某个阈值的时候 ，器件就成为了绝缘体
# -> 低电压，0， False

# 非常非常纯的硅


def nand(a, b):
    '''mocking a pyhsical unit'''
    return 0 if a == b == 1 else 1


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
    a = and_(in_, notSel)
    b = and_(in_, sel)
    
    return a, b
    
def not16(in_):
    # in_: [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0]

    out = [None] * 16

    out[0] = not_(in_[0])
    out[1] = not_(in_[1])
    out[2] = not_(in_[2])
    out[3] = not_(in_[3])
    out[4] = not_(in_[4])
    out[5] = not_(in_[5])
    out[6] = not_(in_[6])
    out[7] = not_(in_[7])
    out[8] = not_(in_[8])
    out[9] = not_(in_[9])
    out[10] = not_(in_[10])
    out[11] = not_(in_[11])
    out[12] = not_(in_[12])
    out[13] = not_(in_[13])
    out[14] = not_(in_[14])
    out[15] = not_(in_[15])

    return out


def and16(a, b):
    
    out = [None] * 16

    out[0] = and_(a[0], b[0])
    out[1] = and_(a[1], b[1])
    out[2] = and_(a[2], b[2])
    out[3] = and_(a[3], b[3])
    out[4] = and_(a[4], b[4])
    out[5] = and_(a[5], b[5])
    out[6] = and_(a[6], b[6])
    out[7] = and_(a[7], b[7])
    out[8] = and_(a[8], b[8])
    out[9] = and_(a[9], b[9])
    out[10] = and_(a[10], b[10])
    out[11] = and_(a[11], b[11])
    out[12] = and_(a[12], b[12])
    out[13] = and_(a[13], b[13])
    out[14] = and_(a[14], b[14])
    out[15] = and_(a[15], b[15])

    return out


def or16(a, b):
    out = [None] * 16

    out[0] = or_(a[0], b[0])
    out[1] = or_(a[1], b[1])
    out[2] = or_(a[2], b[2])
    out[3] = or_(a[3], b[3])
    out[4] = or_(a[4], b[4])
    out[5] = or_(a[5], b[5])
    out[6] = or_(a[6], b[6])
    out[7] = or_(a[7], b[7])
    out[8] = or_(a[8], b[8])
    out[9] = or_(a[9], b[9])
    out[10] = or_(a[10], b[10])
    out[11] = or_(a[11], b[11])
    out[12] = or_(a[12], b[12])
    out[13] = or_(a[13], b[13])
    out[14] = or_(a[14], b[14])
    out[15] = or_(a[15], b[15])

    return out
   
def mux16(a, b, sel):
    out = [None] * 16
    
    out[0] = mux(a[0], b[0], sel=sel)
    out[1] = mux(a[1], b[1], sel=sel)
    out[2] = mux(a[2], b[2], sel=sel)
    out[3] = mux(a[3], b[3], sel=sel)
    out[4] = mux(a[4], b[4], sel=sel)
    out[5] = mux(a[5], b[5], sel=sel)
    out[6] = mux(a[6], b[6], sel=sel)
    out[7] = mux(a[7], b[7], sel=sel)
    out[8] = mux(a[8], b[8], sel=sel)
    out[9] = mux(a[9], b[9], sel=sel)
    out[10] = mux(a[10], b[10], sel=sel)
    out[11] = mux(a[11], b[11], sel=sel)
    out[12] = mux(a[12], b[12], sel=sel)
    out[13] = mux(a[13], b[13], sel=sel)
    out[14] = mux(a[14], b[14], sel=sel)
    out[15] = mux(a[15], b[15], sel=sel)
    
    return out


def or8way(in_):
    # (in_[0] or in_[1] or in[2] .. or in[7])

    or1 = or_(in_[0], in_[1])
    or2 = or_(or1, in_[2])
    or3 = or_(or1, in_[3])
    or4 = or_(or1, in_[4])
    or5 = or_(or1, in_[5])
    or6 = or_(or1, in_[6])
    or7 = or_(or1, in_[7])
    
    return or7
    

def mux4Way16(a, b, c, d, sel):
    sel0out = mux16(a, b, sel[0])
    sel0out2 = mux16(c, d, sel[0])
    out = mux16(sel0out, sel0out2, sel[1])

    return out

def mux8Way16(a, b, c, d, e, f, g, h, sel):
    muxOut1 = mux4Way16(a, b, c, d, sel[0:2])
    muxOut2 = mux4Way16(e, g, g, h, sel[0:2])
    out = mux16(muxOut1, muxOut2, sel[2])

    return out

    
def dmux4way(in_, sel):
    amid, bmid = dmux(in_, sel[0])
    cmid, dmid = dmux(in_, sel[1])
    c = and_(sel[1], cmid)
    d = and_(sel[1], dmid)
    notSel = not_(sel[1])
    a = and_(amid, notSel)
    b = and_(bmid, notSel)
    
    return a, b, c, d


def dmux8way(in_, sel):
    amid, bmid, cmid, dmid = dmux4way(in_, sel[0:2])
    emid, fmid, gmid, hmid = dmux4way(in_, sel[0:2])
    
    notSel1 = not_(sel[2])
    
    a = and_(amid, notSel1)
    b = and_(bmid, notSel1)
    c = and_(cmid, notSel1)
    d = and_(dmid, notSel1)

    e = and_(emid, sel[2])
    f = and_(fmid, sel[2])
    g = and_(gmid, sel[2])
    h = and_(hmid, sel[2])

    return a, b, c, d, e, f, g, h



assert nand(0, 0) == 1
assert nand(1, 0) == 1
assert nand(0, 1) == 1
assert nand(1, 1) == 0
assert not_(0) == 1
assert not_(1) == 0
assert and_(0, 1) == 0
assert and_(1, 1) == 1
assert and_(1, 0) == 0
assert and_(0, 0) == 0
assert or_(0, 0) == 0
assert or_(1, 0) == 1
assert or_(0, 1) == 1
assert or_(1, 1) == 1
assert xor_(0, 0) == 0
assert xor_(1, 1) == 0
assert xor_(1, 0) == 1
assert xor_(0, 1) == 1
assert mux(0, 0, 0) == 0
assert mux(1, 0, 0) == 1
assert mux(1, 1, 0) == 1
assert mux(0, 1, 0) == 0
assert mux(0, 0, 1) == 0
assert mux(1, 0, 1) == 0
assert mux(1, 1, 1) == 1
assert mux(0, 1, 1) == 1

assert dmux(0, 0) == (0, 0)
assert dmux(1, 0) == (1, 0)
assert dmux(0, 1) == (0, 0)
assert dmux(1, 1) == (0, 1)

if __name__ == '__main__':
    print(mux4Way16([0] * 16, [1] * 16, [1] * 16, [1]*16, sel=[0, 0]))
    print(mux4Way16([1] * 16, [0] * 16, [1] * 16, [1]*16, sel=[1, 0]))
    print(mux4Way16([1] * 16, [1] * 16, [0] * 16, [1]*16, sel=[0, 1]))
    print(mux4Way16([1] * 16, [1] * 16, [1] * 16, [0]*16, sel=[1, 1]))
    print(dmux4way(1, [0, 0]))
    print(dmux4way(1, [1, 0]))
    print(dmux4way(1, [1, 1]))
    print(dmux4way(1, [0, 1]))
    print(dmux8way(1, [0, 0, 0]))
    print(dmux8way(1, [0, 0, 1]))
    print(dmux8way(1, [0, 1, 0]))
    print(dmux8way(1, [1, 0, 0]))
    print(dmux8way(1, [0, 1, 1]))
    print(dmux8way(1, [1, 1, 0]))
    print(dmux8way(1, [1, 0, 1]))
    print(dmux8way(1, [1, 1, 1]))


    print('test done!')
