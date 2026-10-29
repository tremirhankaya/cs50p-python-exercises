def main():
    sentence = input("Enter a sentence: ")
    print(convert(sentence))


def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence


main()
