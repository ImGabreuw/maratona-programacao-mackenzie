rules = [0.0, 2000.0, 3000.0, 4500.0]
tax = [0.0, 0.08, 0.18, 0.28]


def entry():
    income = float(input())
    ir = 0.0

    if income <= 2000.0:
        print("Isento")
        return

    for index, rule in enumerate(rules):
        if income > rule:
            if index + 1 < len(rules) and income >= rules[index + 1]:
                ir += (rules[index + 1] - rule) * tax[index]
                continue

            ir += (income - rule) * tax[index]

    print("R$ %.2f" % ir)


if __name__ == '__main__':
    entry()
