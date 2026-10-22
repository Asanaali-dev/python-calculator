OPERATORS = ["+", "-", "*", "/", "**"]


def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        return a / b
    elif op == "**":
        return a ** b


def main():
    history = []

    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно ввести число")
            continue

        op = input("Действие (+, -, *, /, **): ")
        if op not in OPERATORS:
            print("Неизвестное действие")
            continue

        try:
            result = calculate(a, b, op)
        except ZeroDivisionError as error:
            print(error)
        except OverflowError:
            print("Слишком большое число")
        else:
            record = f"{a} {op} {b} = {result}"
            print(record)
            history.append(record)

        again = input("Посчитать ещё? (да/нет): ")
        if again.lower() != "да":
            break

    print("\nИстория вычислений:")
    for line in history:
        print(line)


if __name__ == "__main__":
    main()
