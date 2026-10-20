while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    op = input("Действие (+, -, *, /, **): ")
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print(a / b)
    elif op == "**":
        print(a ** b)
    else:
        print("Неизвестное действие")

    again = input("Посчитать ещё? (да/нет): ")
    if again.lower() != "да":
        break
