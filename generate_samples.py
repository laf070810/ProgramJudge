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


if __name__ == '__main__':
    generate_samples_week1ex4()
