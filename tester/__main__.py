from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path

parser = ArgumentParser(description='Фреймворк для запуска тестов')
parser.add_argument('task', metavar='task', help='Имя каталога для запуска тестов')
parser.add_argument('-c', '--cases', help='Путь к каталогу с тестами относительно module', default='cases')
parser.add_argument('-i', '--input_ext', help='Разрешение файлов входных данных', default='.in')
parser.add_argument('-o', '--output_ext', help='Разрешение файлов результатов', default='.out')
parser.add_argument('-m', '--module', help='Модуль python с кодом решения задачи', default='main')
parser.add_argument('-f', '--function', help='Имя функции в модуле', default='main')
parser.add_argument('-d', '--description', help='Путь к файлу с описанием задачи', default='problem.txt')
parser.add_argument('-t', '--tests', help='Список имен файлов для тестов, разделенных запятой', default=None)


def main(
        task: str,
        cases: str = 'cases',
        input_ext: str = '.in',
        output_ext: str = '.out',
        module_name: str = 'main',
        function_name: str = 'main',
        description_path: str | None = None,
        tests: str | None = None
):
    module = import_module(f'{task}.{module_name}')
    solution = getattr(module, function_name)

    path = Path(f'{task}/{cases}')

    if description_path:
        with open(f'{task}/{description_path}') as fp:
            print(fp.read())

    cases = path.glob(f'*{input_ext}')
    if tests is not None:
        files = set([f'{name.strip()}{input_ext}' for name in tests.split(',')])
        cases = [case for case in cases if case.name in files]

    for case in cases:
        print('-' * 10)
        case_name = case.name.removesuffix(input_ext)
        print(case_name)
        print('-' * 10)

        with open(next(path.glob(f'{case_name}{output_ext}'))) as fp:
            expected = fp.readline().strip()

        with open(case) as fp:
            data = fp.readlines()

        print(f'Входные данные: {" ".join(data)}')
        print(f'Ожидается: {expected}')

        actual = solution(data)
        print(f'Получено: {actual}')

        if actual == expected:
            print('Тест пройден')
        else:
            print('ОШИБКА: Тест не пройден')


if __name__ == '__main__':
    args = parser.parse_args()
    main(
        args.task,
        cases=args.cases,
        input_ext=args.input_ext,
        output_ext=args.output_ext,
        module_name=args.module,
        function_name=args.function,
        description_path=args.description,
        tests=args.tests
    )
