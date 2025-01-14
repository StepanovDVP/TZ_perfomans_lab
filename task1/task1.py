import argparse


def task1(n: int, m: int) -> str:
    if n <= 0 or m <= 0:
        return ''

    lst = list(range(1, n + 1))
    s = ''.join(map(str, lst))
    i = 0
    res = []
    interval_enums = []
    while True:
        interval_enums.append(s[i])
        i += 1

        if m == len(interval_enums):
            current = ''.join(interval_enums)

            if res and current == res[0]:
                break

            res.append(current)
            interval_enums.clear()
            i -= 1

        if i == len(s):
            i = 0
    return ''.join(map(lambda x: x[0], res))


def main():
    parser = argparse.ArgumentParser(description='Задание 1')
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)

    args = parser.parse_args()
    res = task1(args.n, args.m)
    print(res)


if __name__ == '__main__':
    main()
