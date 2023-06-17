# execution time: 0.208s

import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='latin_1')

if __name__ == '__main__':
    def filter_num_or_dot(raw_input: str) -> str:
        cleaned_input = "".join([char for char in raw_input if char.isnumeric() or char == "."])

        if cleaned_input.count(".") == 0:
            return cleaned_input

        return cleaned_input[:cleaned_input.index(".") + 3]


    input_1 = filter_num_or_dot(input())
    input_2 = filter_num_or_dot(input())

    cpf = input_1[0:11]
    num_1 = float(input_1[11:])
    num_2 = float(input_2)

    print("cpf", cpf)
    print(f"{num_1 + num_2:.2f}")
