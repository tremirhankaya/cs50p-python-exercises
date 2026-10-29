def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number_seen = False
    index = 0

    if not s.isalnum():
        return False
    if 6 < len(s) or len(s) < 2:
        return False
    for c in s:
        if not number_seen and c.isnumeric():
            number_seen = True
            if c == "0":
                return False
        if number_seen and not c.isnumeric():
            return False
        if index < 2 and c.isnumeric():
            return False

        index += 1

    return True


main()
