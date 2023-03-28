def entry():
    while True:
        try:
            sentence = input()

            dancing_sentence = ""
            index = 0

            for char in sentence:
                if char == " ":
                    dancing_sentence += char
                    continue

                if index % 2 == 0:
                    dancing_sentence += char.upper()
                else:
                    dancing_sentence += char.lower()

                index += 1

            print(dancing_sentence)
        except EOFError:
            break


if __name__ == '__main__':
    entry()
