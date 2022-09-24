from typing import TextIO
from os import rename, remove
from random import randint


def make_test_file(n: int, t: int, filename: str = 'unsorted.tmp'):
    numbers = (f'{randint(0, t)}\n' for _ in range(n))

    with open(filename, 'w') as fp:
        fp.writelines(numbers)


def read_int(source: TextIO) -> int | None:
    line = source.readline()
    if line == '':
        return None

    return int(line.strip())


def write_int(dest: TextIO, num: int):
    dest.write(f'{num}\n')


def chunk_split_by_two_files(source: TextIO, first: TextIO, second: TextIO, batch_size: int = 10):
    eof, write_into_first = False, True
    while not eof:
        numbers = []
        for _ in range(batch_size):
            num = read_int(source)
            if num is None:
                eof = True
                break
            numbers.append(num)

        numbers = sorted(numbers)
        target = first if write_into_first else second
        for num in numbers:
            write_int(target, num)
        write_into_first = not write_into_first


def part_merge(dest: TextIO, first: TextIO, second: TextIO):
    first_item, second_item = read_int(first), read_int(second)

    while first_item is not None and second_item is not None:
        if first_item < second_item:
            write_int(dest, first_item)
            first_item = read_int(first)
        else:
            write_int(dest, second_item)
            second_item = read_int(second)

    while first_item is not None:
        write_int(dest, first_item)
        first_item = read_int(first)

    while second_item is not None:
        write_int(dest, second_item)
        second_item = read_int(second)


def split_by_two_files(source: TextIO, first: TextIO, second: TextIO):
    write_first_only, write_into_first = True, True
    last_num = float('-inf')
    while last_num is not None:
        num = read_int(source)
        if num is None:
            break

        if num < last_num:
            write_first_only = False
            write_into_first = not write_into_first

        target = first if write_into_first else second
        write_int(target, num)
        last_num = num

    return write_first_only


def external1(
        t: int = 100,
        input_name: str = 'unsorted.tmp',
        output_name: str = 'sorted.tmp'
):
    file_names = [f'{i}.tmp' for i in range(t + 1)]
    file_pointers = [open(name, 'w') for name in file_names]

    with open(input_name) as source:
        num = read_int(source)
        while num is not None:
            output = file_pointers[int(num)]
            write_int(output, num)
            num = read_int(source)

    for fp in file_pointers:
        fp.close()

    file_pointers = [open(name) for name in file_names]

    with open(output_name, 'w') as dest:
        for source in file_pointers:
            num = read_int(source)
            while num is not None:
                write_int(dest, num)
                num = read_int(source)

    for fp in file_pointers:
        fp.close()

    for name in file_names:
        remove(name)


def external2(
        input_name: str = 'unsorted.tmp',
        output_name: str = 'sorted.tmp',
):
    first_run, already_sorted = True, False
    while not already_sorted:
        name = input_name if first_run else output_name
        with open(name) as fp, open('1.tmp', 'w') as first, open('2.tmp', 'w') as second:
            already_sorted = split_by_two_files(fp, first, second)

        with open(output_name, 'w') as fp, open('1.tmp') as first, open('2.tmp') as second:
            part_merge(fp, first, second)

        first_run = False

    remove('1.tmp')
    remove('2.tmp')


def external3(
        input_name: str = 'unsorted.tmp',
        output_name: str = 'sorted.tmp',
        batch_size: int = 10
):
    with open(input_name) as fp, open('1.tmp', 'w') as first, open('2.tmp', 'w') as second:
        chunk_split_by_two_files(fp, first, second, batch_size)

    already_sorted = False
    while not already_sorted:
        with open(output_name, 'w') as for_merge, open('1.tmp') as first, open('2.tmp') as second:
            part_merge(for_merge, first, second)

        with open(output_name) as for_split, open('1.tmp', 'w') as first, open('2.tmp', 'w') as second:
            already_sorted = split_by_two_files(for_split, first, second)

    remove(output_name)
    rename('1.tmp', output_name)
    remove('2.tmp')
