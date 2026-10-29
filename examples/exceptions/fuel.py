def main():
    while True:
        fraction = input("Fraction: ")

        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x > y or x < 0:
                raise ValueError
            break
        except ValueError:
            pass

    calculate(x, y)


def calculate(x, y):

    percentage = round((x / y) * 100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


main()
