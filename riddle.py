import itertools

# print(f'{10:04}')

def slice_as_str(N):
    ret = ''

    for n in N:
        ret += str(n)

    return ret


def slice_as_num(N):
    ret = ''

    for n in N:
        ret += str(n)

    return int(ret)


def lists(n):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    permutations = list(itertools.permutations(numbers))

    count = 0

    for i in permutations:
        numerator_str = slice_as_str(i[:5])
        denominator_str = slice_as_str(i[5:])

        numerator = slice_as_num(i[:5])
        denominator = slice_as_num(i[5:])

        if (numerator / denominator) == n:
            count += 1
            print(numerator_str + " / " + denominator_str + " = " + str(n))

    if count == 0:
        print("There are no solutions for N")

N = 80
lists(N)
