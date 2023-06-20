if __name__ == '__main__':
    count_selected = 0
    previous_selected = ""

    for _ in range(int(input())):
        v = input()
        if previous_selected != v:
            previous_selected = v
            count_selected += 1

    print(count_selected)

