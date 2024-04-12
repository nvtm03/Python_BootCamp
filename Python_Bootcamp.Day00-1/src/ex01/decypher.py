import sys


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        error()
    else:
        print(make_word(args[1]))


def error() -> None:
    print('Error!!! \nThere must be two arguments')


def make_word(string: str) -> str:
    result: str = ''
    for word in string.split():
        result += word[0]
    return result


if __name__ == '__main__':
    main()
