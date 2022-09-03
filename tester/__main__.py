from argparse import ArgumentParser, BooleanOptionalAction
from importlib import import_module
from dataclasses import dataclass
from time import monotonic
from pathlib import Path

from .timeout import timeout_deco

parser = ArgumentParser(description='Фреймворк для запуска тестов')
parser.add_argument('task', metavar='task', help='Имя каталога для запуска тестов')
parser.add_argument('-c', '--cases', help='Путь к каталогу с тестами относительно module', default='cases')
parser.add_argument('-i', '--input_ext', help='Разрешение файлов входных данных', default='.in')
parser.add_argument('-o', '--output_ext', help='Разрешение файлов результатов', default='.out')
parser.add_argument('-m', '--module', help='Модуль python с кодом решения задачи', default='main')
parser.add_argument('-f', '--function', help='Имя функции в модуле', default='main')
parser.add_argument('-d', '--description', help='Путь к файлу с описанием задачи', default='problem.txt')
parser.add_argument('-t', '--tests', help='Список имен файлов для тестов, разделенных запятой', default=None)
parser.add_argument('-s', '--short', help='Сокращенный формат вывода', type=bool,
                    action=BooleanOptionalAction, default=False)
parser.add_argument('--timeout', help='Максимальное время выполнения функции (секунды)', type=int, default=5)


@dataclass
class CaseResult:
    expected: str | None = None
    time: int | None = None
    exc: Exception | None = None
    actual: str | None = None

    @property
    def success(self) -> bool:
        return self.actual == self.expected and self.actual is not None


@dataclass
class Case:
    name: str
    input_path: Path
    output_path: Path
    result: CaseResult | None = None

    def input(self) -> list[str]:
        with open(self.input_path) as fp:
            return fp.readlines()

    def output(self) -> str:
        with open(self.output_path) as fp:
            return fp.readline().strip()


def main(
        task: str,
        cases: str = 'cases',
        input_ext: str = '.in',
        output_ext: str = '.out',
        module_name: str = 'main',
        function_name: str = 'main',
        description_path: str | None = None,
        short: bool = False,
        timeout: int = 5,
        tests: str | None = None
):
    task_path = task.replace('.', '/')

    if description_path:
        with open(f'{task_path}/{description_path}') as fp:
            print(fp.read())

    path = Path(f'{task_path}/{cases}')
    cases = get_cases(path, input_ext, output_ext, tests)

    module = import_module(f'{task}.{module_name}')
    solution = getattr(module, function_name)
    solution = timeout_deco(timeout)(solution)

    for case in sorted(cases, key=lambda x: x.name):
        result = CaseResult()

        result.expected = case.output()
        start = monotonic()
        try:
            result.actual = solution(case.input())
        except Exception as e:
            result.exc = e

        result.time = monotonic() - start

        case.result = result
        if short:
            short_display_case(case)
        else:
            display_case(case)


def get_cases(path: Path, input_ext: str, output_ext: str, tests: str | None = None) -> list[Case]:
    case_paths = path.glob(f'*{input_ext}')
    if tests is not None:
        files = set([f'{name.strip()}{input_ext}' for name in tests.split(',')])
        case_paths = [case_path for case_path in case_paths if case_path.name in files]

    cases = []
    for case_path in case_paths:
        name = case_path.name.removesuffix(input_ext)
        cases.append(Case(
            name=name,
            input_path=case_path,
            output_path=next(path.glob(f'{name}{output_ext}'))
        ))

    return cases


def display_case(case: Case):
    print('-' * 10)
    print(case.name)
    print('-' * 10)

    print(f'Входные данные: {" ".join(case.input())}')
    print(f'Ожидается: {case.result.expected}')
    print(f'Получено:  {case.result.actual}')
    print(f'Время выполнения: {(case.result.time * 1000):.4f} ms')

    if case.result.success:
        print('Тест пройден')
    else:
        print(f'ОШИБКА: Тест не пройден: {str(case.result.exc) if case.result.exc else ""}')


def short_display_case(case: Case):
    print('-' * 10)
    print(case.name)
    print(f'Время выполнения: {(case.result.time * 1000):.4f} ms')
    if case.result.success:
        print('Тест пройден')
    else:
        print(f'ОШИБКА: Тест не пройден: {str(case.result.exc) if case.result.exc else ""}')
    print('-' * 10)

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
        tests=args.tests,
        short=args.short,
        timeout=args.timeout
    )
