import argparse
from typing import List, Tuple
from decimal import Decimal

from constants import (
    EXCEPTION_VALUE, EXCEPTION_CIRCLE_FILE, POSITION_IN,
    POSITION_ON, POSITION_OUT

)


def read_file(file_path: str) -> List[Tuple[Decimal, ...]]:
    """Прочитать данные из файла."""
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            if numbers:
                try:
                    result.append(tuple(map(Decimal, numbers)))
                except ValueError:
                    print(f'{EXCEPTION_VALUE}{line}')
                    raise
    return result


def check_points(
        x1: Decimal, y1: Decimal,
        r: Decimal, xc: Decimal, yc: Decimal
) -> int:
    """Проверить положение точки относительно окружности."""
    res = (x1 - xc) ** 2 + (y1 - yc) ** 2
    if res < r ** 2:
        return POSITION_IN
    elif res > r ** 2:
        return POSITION_OUT
    else:
        return POSITION_ON


def task2(path_circle: str, path_points: str):
    """Основная функция выполнения задачи."""
    circle = read_file(path_circle)
    if len(circle) != 2:
        print(EXCEPTION_CIRCLE_FILE)
        return
    x, y = circle[0]
    radius = circle[1][0]

    points = read_file(path_points)

    res = [
        check_points(x, y, radius, xc, yc)
        for xc, yc in points
    ]

    for r in res:
        print(r)


def main():
    parser = argparse.ArgumentParser(description='Задание 2')
    parser.add_argument('circle_file', type=str)
    parser.add_argument('points_file', type=str)

    args = parser.parse_args()

    task2(args.circle_file, args.points_file)


if __name__ == '__main__':
    main()
