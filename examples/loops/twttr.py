vowels = ["a", "e", "i", "o", "u"]


def toTwitter(s):
    my_list = []
    for c in s:
        if not c.lower() in vowels:
            my_list.append(c)

    return "".join(my_list)


def main():
    s = input("Input: ")
    print("Output: " + toTwitter(s))


main()
