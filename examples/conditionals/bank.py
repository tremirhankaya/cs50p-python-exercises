def main():
    print(f"${greet(input('Greeting: '))}")


def greet(sentence):
    sentence = sentence.strip().lower()
    if sentence.startswith("hello"):
        return 0
    elif sentence.startswith("h"):
        return 20
    else:
        return 100


main()
