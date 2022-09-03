AFTER_DOT = 11


def format_result(result: float) -> str:
    result = f'{result:.{AFTER_DOT}f}'

    zero_counter = 0
    for chr in reversed(result):
        if chr == '0':
            zero_counter += 1
        elif chr == '.':
            zero_counter -= 1
        else:
            break

    return result[0: len(result) - zero_counter]
