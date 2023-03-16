import copy


def recursive_replace(text: str) -> str:
    if "<>" not in text:
        return text

    return recursive_replace(text.replace("<>", ""))


def entry():
    n = int(input())
    results = []

    for i in range(n):
        d1 = input().replace(".", "").replace(",", "")
        d2 = recursive_replace(copy.copy(d1))

        results.append(int((len(d1) - len(d2)) / 2))

    print("\n".join([str(i) for i in results]))


if __name__ == '__main__':
    entry()
