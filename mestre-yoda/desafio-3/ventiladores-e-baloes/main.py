from typing import List


def get_near_fans(line: List[int], balloon_position: int) -> List[int]:
    near_fans = []

    for i in range(balloon_position - 1, -1, -1):
        slot = line[i]
        if slot != 0 and len(near_fans) < 2:
            near_fans.append(slot)

    for i in range(balloon_position + 1, len(line)):
        slot = line[i]
        if slot != 0 and len(near_fans) < 2:
            near_fans.append(slot)

    return near_fans


def entry():
    l, c, p = [int(i) for i in input().split()]

    matrix = []

    for i in range(l):
        line = [int(i) for i in input().split()]

        matrix.append(line)
        index = matrix[i].index("balao") if "balao" in matrix[i] else p - 1
        right_fan, left_fan = get_near_fans(line, index)
        p = index + (right_fan - left_fan)
        matrix[i][p] = "balao"

        if p == line.index(right_fan) or line.index(left_fan):
            print(f"BOOM {i + 1} {p}")

    print(matrix)


if __name__ == '__main__':
    entry()
