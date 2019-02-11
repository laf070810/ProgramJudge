def generate_samples_week1ex1():
    with open('input_1.txt', 'w') as input:
        pass
    with open('output_1.txt', 'w') as output:
        pass


def generate_samples_week1ex2():
    with open('input_2.txt', 'w') as input:
        pass
    with open('output_2.txt', 'w') as output:
        pass


def generate_samples_week1ex3():
    with open('input_3.txt', 'w') as input:
        pass
    with open('output_3.txt', 'w') as output:
        pass


def generate_samples_week1ex4():
    with open('input_4.txt', 'w') as input:
        input.write('0')
    with open('output_4.txt', 'w') as output:
        output.writelines(['14\n',
                           '   Nine-by-nine Multiplication Table   \n',
                           '---------------------------------------\n',
                           '     1   2   3   4   5   6   7   8   9 \n',
                           '---------------------------------------\n',
                           ' 1   1   2   3   4   5   6   7   8   9 \n',
                           ' 2       4   6   8  10  12  14  16  18 \n',
                           ' 3           9  12  15  18  21  24  27 \n',
                           ' 4              16  20  24  28  32  36 \n',
                           ' 5                  25  30  35  40  45 \n',
                           ' 6                      36  42  48  54 \n',
                           ' 7                          49  56  63 \n',
                           ' 8                              64  72 \n',
                           ' 9                                  81 \n',
                           '---------------------------------------'])


def generate_samples_week2ex1():
    with open('input_1.txt', 'w') as input:
        for i in range(50):
            input.write('51\n')
            input.write('50\n')
            for j in range(50):
                input.write(str(i + 1) + ' ' + str(j + 1) + '\n')

    with open('output_1.txt', 'w') as output:
        for i in range(50):
            output.write(str((i + 1) * 50) + '\n')
            for j in range(50):
                for k in range(i + 1):
                    output.write('*' * (2 * k + 1) + ' ' * (j + 1) + '*' * (2 * (i - k) + 1) + '\n')


def generate_samples_week2ex2():
    with open('input_2.txt', 'w') as input:
        with open('output_2.txt', 'w') as output:
            import random
            for _ in range(100):
                k = random.randint(1, 1000)
                input.write(str(k + 1) + '\n')
                input.write(str(k) + '\n')
                output.write(str(k) + '\n')
                for i in range(k):
                    a = random.randint(-1000000000, 1000000000)
                    b = random.randint(-1000000000, 1000000000)
                    input.write(str(a) + ' ' + str(b) + '\n')
                    output.write(str(b) + ' ' + str(a) + '\n')


def generate_samples_week2ex3():
    primes = []
    for i in range(2, 1000000000):
        if isPrime(i):
            primes.append(i)
        if i % 10000 == 0:
            print(str(i) + ' ' + str(len(primes)))
        if len(primes) > 2000:
            break

    import random
    with open('input_3.txt', 'w') as input:
        with open('output_3.txt', 'w') as output:
            for i in range(10):
                input.write('11' + '\n')
                input.write('10' + '\n')
                output.write('10' + '\n')
                for j in range(10):
                    a = random.randint(1, 2000)
                    input.write(str(a) + '\n')
                    output.write(str(primes[a - 1]) + '\n')


def generate_samples_week2ex4():
    import random

    with open('input_4.txt', 'w') as input:
        with open('output_4.txt', 'w') as output:
            for i in range(10):
                input.write('11' + '\n')
                input.write('10' + '\n')
                output.write('10' + '\n')
                for j in range(10):
                    a = random.randint(1, 10000)
                    b = random.randint(1, 10000)
                    gcd, lcm = gcdlcm(a, b)
                    input.write(str(a) + ' ' + str(b) + '\n')
                    output.write(str(gcd) + ' ' + str(lcm) + '\n')


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcdlcm(a, b):
    a0, b0 = a, b
    if (b > a):
        a, b = b, a
    while(a % b != 0):
        a = a % b
        a, b = b, a
    return b, a0 * b0 // b


if __name__ == '__main__':
    generate_samples_week2ex3()