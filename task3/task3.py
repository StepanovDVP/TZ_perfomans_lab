import argparse
import json
from typing import Any


def read_values(path: str) -> dict[int, str]:
    """Чтение values.json, извлечение ID и их значений."""
    with open(path, 'r') as file:
        data = json.load(file)
        if 'values' not in data:
            raise ValueError(f'Файл {path} не содержит ключ "values".')
        return {
            test['id']: test.get('value', None)
            for test in data['values']
        }


def read_tests(path: str) -> dict[str, list[dict[str, Any]]]:
    """Чтение tests.json."""
    with open(path, 'r') as file:
        return json.load(file)


def get_result_test(
        lst: list[dict[str, Any]],
        value: dict[int, str]
) -> list[dict[str, Any]]:
    """Рекурсивное заполнение ключей 'value'."""
    for dct in lst:
        if 'value' in dct:
            dct['value'] = value.get(dct['id'], dct['value'])
        if 'values' in dct:
            get_result_test(dct['values'], value)
    return lst


def create_report(path: str, data: dict[str, list[dict[str, Any]]]):
    """Сохранение результата в report.json."""
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def task3(path_values: str, path_tests: str, path_report: str):
    """Основная функция выполнения задачи."""
    values = read_values(path_values)
    tests = read_tests(path_tests)

    if not isinstance(tests, dict) or len(tests) != 1:
        raise ValueError('Файл tests.json должен содержать только один корневой элемент.')

    key, tests_structure = next(iter(tests.items()))
    data_dct = {key: get_result_test(tests_structure, values)}
    create_report(path_report, data_dct)


def main():
    parser = argparse.ArgumentParser(description='Задание 3')
    parser.add_argument('path_values', type=str)
    parser.add_argument('path_tests', type=str)
    parser.add_argument('path_report', type=str)

    args = parser.parse_args()

    task3(args.path_values, args.path_tests, args.path_report)


if __name__ == '__main__':
    main()
