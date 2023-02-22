from math import sqrt
 
 
def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False
 
 
def store():
    filenames = ['a.txt', 'b.txt', 'c.txt']
    f_list = []
    for filename in filenames:
        f_list.append(open(filename, 'w', encoding='utf-8'))
    for number in range(1, 10000):
        if number < 100 and is_prime(number):
            f_list[0].write(str(number) + '\n')
        elif number < 1000 and is_prime(number):
            f_list[1].write(str(number) + '\n')
        elif is_prime(number):
            f_list[2].write(str(number) + '\n')
 
 
if __name__ == '__main__':
    store()
