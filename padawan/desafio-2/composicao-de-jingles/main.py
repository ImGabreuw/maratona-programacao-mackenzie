notes = {
    "W": 1,
    "H": 1 / 2,
    "Q": 1 / 4,
    "E": 1 / 8,
    "S": 1 / 16,
    "T": 1 / 32,
    "X": 1 / 64
}


def entry():
    correct_compasses = []

    while True:
        raw = input()

        if raw == "*":
            break

        compasses = raw.split("/")
        count = 0

        for compass in compasses:
            duration = 0

            for note in compass:
                duration += notes[note]

            if duration == 1:
                count += 1

        correct_compasses.append(count)

    for result in correct_compasses:
        print(result)


if __name__ == '__main__':
    entry()
