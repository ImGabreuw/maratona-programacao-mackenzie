# execution time: 0.011s

import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='latin_1')

if __name__ == '__main__':
    def clean_input(raw_input: str) -> str:
        cleaned_input = "".join([char for char in raw_input if char.isnumeric() or char == "."])

        dot_index = cleaned_input.find(".")

        if dot_index == -1:
            return cleaned_input

        return cleaned_input[:dot_index + 3]


    input_1 = clean_input(input())
    input_2 = clean_input(input())

    cpf = input_1[:11]
    num_1 = float(input_1[11:])
    num_2 = float(input_2)

    print("cpf", cpf)
    print(f"{num_1 + num_2:.2f}")
