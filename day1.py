# https://adventofcode.com/2020/day/1

from pathlib import Path

FOLDER = "inputs/"
INPUT_FILE = "day1.txt"
SUM = 2020


class Day1:
    def __init__(self):
        # making the file path universally compatible with pathlib
        folder = Path(FOLDER)
        file_to_open = folder / INPUT_FILE

        # input file opening and reading
        with open(file_to_open) as file:
            file_input = file.read()
            self.data = file_input.split()

        self.data_len = len(self.data)

        # print(self.data)

        self.day1()

        print(f'Day 1, Part 1: {self.day1()}')

    def day1(self):
        for i in range(0, self.data_len):
            aux = int(self.data[i])
            # print(type(aux))
            for element in self.data[i + 1:]:
                aux2 = int(element)
                if aux + aux2 == SUM:
                    answer = aux * aux2
                    return answer
