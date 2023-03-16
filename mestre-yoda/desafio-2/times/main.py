def entry():
    n, t = [int(i) for i in input().split(" ")]
    people = dict()

    for i in range(n):
        name, skill = input().split(" ")
        people[name] = int(skill)

    people = dict(sorted(
        people.items(),
        key=lambda element: element[1]
    ))

    teams = [list() for i in range(t)]
    current_team = 1

    for i in range(n):
        if current_team > t:
            current_team = 1

        teams[current_team - 1].append(people.popitem()[0])
        current_team += 1

    for i, team in enumerate(teams):
        print(f'Time {i + 1}\n' + "\n".join(sorted(team)) + "\n")


if __name__ == '__main__':
    entry()
