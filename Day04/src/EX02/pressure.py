from time import sleep
from random import randint


def emit_gel(step: int):
    num = 21
    while num <= 100:
        step_sign = yield num
        num += step_sign * randint(0, step)


def valve(step: int):
    gen_pressure = emit_gel(step)
    cnt_pressure = next(gen_pressure)
    print(cnt_pressure)
    sign = 1
    while True:
        if cnt_pressure < 10 or cnt_pressure > 90:
            gen_pressure.close()
            break
        if cnt_pressure < 20:
            sign = 1
        elif cnt_pressure > 80:
            sign = -1
        cnt_pressure = gen_pressure.send(sign)
        print(cnt_pressure)
        sleep(1)


if __name__ == '__main__':
    valve(20)
