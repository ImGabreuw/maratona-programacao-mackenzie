sides = []

for rawSide in input().split(" "):
    sides.append(float(rawSide))

sides.sort()


def side_classification(sides_square):
    set_sides = set(sides_square)

    if len(set_sides) == 1:
        print("TRIANGULO EQUILATERO")
        return

    if len(set_sides) == 2:
        print("TRIANGULO ISOSCELES")


def angle_classification():
    if sides[2] >= sides[0] + sides[1]:
        print("NAO FORMA TRIANGULO")
        return

    sides_square = sides.copy()
    sides_square.sort()

    for index, value in enumerate(sides_square):
        sides_square[index] = value ** 2

    if sides_square[2] == sides_square[0] + sides_square[1]:
        print("TRIANGULO RETANGULO")
        side_classification(sides_square)
        return

    if sides_square[2] > sides_square[0] + sides_square[1]:
        print("TRIANGULO OBTUSANGULO")
        side_classification(sides_square)
        return

    print("TRIANGULO ACUTANGULO")
    side_classification(sides_square)


angle_classification()
