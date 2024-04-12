import sys


def check_line(line: str) -> bool:
    if len(line) != 32:
        return False
    first_no_zero: int = 0
    for letter in line:
        if letter != '0':
            break
        first_no_zero += 1
    if first_no_zero != 5:
        return False
    return True


def error() -> None:
    print('Error!!! \nThere must be two arguments')


def main() -> None:
    if len(sys.argv) == 2:
        for _ in range(int(sys.argv[1])):
            line: str = sys.stdin.readline().strip()
            if check_line(line):
                print(line)
    else:
        error()


if __name__ == '__main__':
    main()
