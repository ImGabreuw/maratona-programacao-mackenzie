# Execution time: 0.000s

if __name__ == '__main__':
    p, _ = [int(i) for i in input().split()]
    pipes_height = [int(i) for i in input().split()]

    for i, height in enumerate(pipes_height):
        if i < len(pipes_height) - 1:
            next_pipe = pipes_height[i + 1]

            if height + p < next_pipe or height - p > next_pipe:
                print("GAME OVER")
                break
    else:
        print("YOU WIN")
