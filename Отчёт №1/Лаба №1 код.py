import math


def get_float(prompt):
    value = input(prompt)
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Не число: {value!r}")


def rc_filter_frequency():
    r = get_float("Введите значение R: ")
    c = get_float("Введите значение C: ")
    return 1 / (2 * math.pi * r * c)


if __name__ == "__main__":
    try:
        f = rc_filter_frequency()
        print(f"Частота среза RC-фильтра: {f:.4f} Гц")
    except ValueError as e:
        print("Ошибка:", e)
