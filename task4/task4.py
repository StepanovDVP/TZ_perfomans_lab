import argparse


def read_numbers_from_file(file_path: str) -> list[int]:
    """Чтение чисел из файла."""
    with open(file_path, 'r') as file:
        return [int(number) for number in file if number.strip().isdigit()]


def task4(nums: list[int]) -> int:
    """Рассчитать минимальное количество ходов."""
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


def main():
    parser = argparse.ArgumentParser(description='Задание 4')
    parser.add_argument('file')
    args = parser.parse_args()

    nums = read_numbers_from_file(args.file)
    if not nums:
        raise ValueError('Файл не содержит чисел.')

    result = task4(nums)
    print(result)


if __name__ == "__main__":
    main()
