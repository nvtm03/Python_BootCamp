import sys
from typing import Tuple


def main() -> None:
    error, result = check_lines()
    if error:
        print('Error')
    else:
        print(result)


def check_lines() -> Tuple[bool, bool]:
    row: int = 0
    result: bool = True
    flag_error: bool = False
    for line in sys.stdin:
        line = line.strip()
        if len(line) != 5:
            flag_error = True
            break
        row += 1
        if row == 1:
            result &= (line[0] == '*' and line[1] != '*' and line[2] != '*'
                       and line[3] != '*' and line[4] == '*')
        elif row == 2:
            result &= (line[0] == '*' and line[1] == '*' and line[2] != '*'
                       and line[3] == '*' and line[4] == '*')
        elif row == 3:
            result &= (line[0] == '*' and line[1] != '*' and line[2] == '*'
                       and line[3] != '*' and line[4] == '*')
        else:
            flag_error = True
            break
    if row != 3:
        flag_error = True

    return flag_error, result


if __name__ == '__main__':
    main()
