def nand(in_1, in_2):
    return 0 if in_1 == in_2 == 1 else 1
    
if __name__ == '__main__':
    print(nand(0, 1))
    print(nand(1, 1))
    print(nand(1, 0))
