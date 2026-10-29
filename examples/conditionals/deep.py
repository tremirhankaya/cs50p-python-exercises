def main():
    user_input = input(
        "What is the answer to the Great Question of Life, the Universe and Everything?"
    )
    if is_true(clear_input(user_input)):
        print("Yes")
    else:
        print("No")


def clear_input(sentence):
    return sentence.lower()


def is_true(sentence):
    return sentence in ["forty two", "forty-two", "42"]


main()
