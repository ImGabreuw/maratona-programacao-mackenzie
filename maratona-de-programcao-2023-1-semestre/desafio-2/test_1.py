if __name__ == '__main__':
    input_1, input_2 = input(), input()

    cpf = ""
    num_1, num_2 = "", ""

    i = 0
    for c in input_1:
        if c == ".":
            num_1 += c

        if not c.isnumeric():
            continue

        if i < 11:
            cpf += c
        else:
            num_1 += c

        i += 1

    i = 0
    for c in input_2:
        if c == ".":
            num_2 += c

        if not c.isnumeric():
            continue

        num_2 += c
        i += 1

    print("cpf", cpf)
    print(f"{float(num_1) + float(num_2):.2f}")
