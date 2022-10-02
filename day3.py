# https://adventofcode.com/2020/day/3

from pathlib import Path

FOLDER = "inputs/"
INPUT_FILE = "day3.txt"
TREE = '#'


class Day3:
    def __init__(self):
        # making the file path universally compatible with pathlib
        folder = Path(FOLDER)
        file_to_open = folder / INPUT_FILE

        # input file opening and reading
        with open(file_to_open) as file:
            file_input = file.read()
            self.data = file_input.split()

        print(f'Day 3, Part 1: {self.part1()}')
        print(f'Day 3, Part 2: {self.part2()}')

    def part1(self):
        """
        --- Day 3: Toboggan Trajectory ---
        With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be
        easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to
        see which angles will take you near the fewest trees.

        Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map
        (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#

        These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome
        stability, the same pattern repeats to the right many times:

        ..##.........##.........##.........##.........##.........##.......  --->
        #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
        .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
        ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
        .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
        ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
        .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
        .#........#.#........#.#........#.#........#.#........#.#........#
        #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
        #...##....##...##....##...##....##...##....##...##....##...##....#
        .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

        You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row
        on your map).

        The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational
        numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

        From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the
        position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

        The locations you'd check in the above example are marked here with O where there was an open square and X
        where there was a tree:

        ..##.........##.........##.........##.........##.........##.......  --->
        #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
        .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
        ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
        .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
        ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
        .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
        .#........#.#........X.#........#.#........#.#........#.#........#
        #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
        #...##....##...##....##...#X....##...##....##...##....##...##....#
        .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

        In this example, traversing the map using this slope would cause you to encounter 7 trees.

        Starting in the top-left corner of your map and following a slope of right 3 and down 1, how many trees would
        you encounter?
        """

        # every part of data input is 31 chars long, buy anyway let's check it
        data_len = len(self.data[0])
        '''
        counter = 0
        for element in self.data[1:]:
            if len(element) != data_len:
                counter += 1

        if counter != 0:
            print('not all the elements have the same size')
        else:
            print('all the elements have the same size')
        '''
        # the output was 'all the elements have the same size'

        trees = 0
        i = 0

        for element in self.data[1:]:  # we don't care about the first line of input
            aux = list(element)
            i += 3
            # let's check if we are beyond the right edge of each line. If so, we step back a whole data_len
            # another solution would be to reproduce the input infinite times to the right, or dynamically
            # as needed, but that would have been not too efficient. This approach is way more simple.
            if i >= (data_len - 1):
                i -= data_len
            if aux[i] == TREE:
                trees += 1

        print(f'Day 3, Part 1jfhjv: {self.how_many_trees(3, 1)}')
        return trees

    def part2(self):
        """
        --- Part Two ---
        Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after
        all.

        Determine the number of trees you would encounter if, for each of the following slopes, you start in the
        top-left corner and traverse the map all the way to the bottom:

        Right 1, down 1.
        Right 3, down 1. (This is the slope you already checked.)
        Right 5, down 1.
        Right 7, down 1.
        Right 1, down 2.

        In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together,
        these produce the answer 336.

        What do you get if you multiply together the number of trees encountered on each of the listed slopes?
        """

        # The resolution of Part 2 is basically the same as Part 1, but with other parameters.
        # Thus, we'll create a function that make the work in bots parts.
        # We will create an array of results with all of them, and then they will be multiplied with each other.
        # The parameters follow a geometrical progression (+2, and +1 when the first one did 1,3,5,7), so we can
        # easily automate all the process

        trees = []

        for j in range(1, 8, 2):
            trees.append(self.how_many_trees(j, 1))

        # I won't make special logic in how_many_trees just for 1 case
        trees.append(self.how_many_trees(1, 2))

        print(trees)

        # now let's multiply all the together

        answer = 1

        for element in trees:
            answer *= element

        return answer

    def how_many_trees(self, lateral_step, down_step):
        trees = 0
        data_len = len(self.data[0])
        print(data_len)
        i = 0

        for element in self.data[1::down_step]:  # we don't care about the first line of input
            aux = list(element)
            i += lateral_step
            # let's check if we are beyond the right edge of each line. If so, we step back a whole data_len
            # another solution would be to reproduce the input infinite times to the right, or dynamically
            # as needed, but that would have been not too efficient. This approach is way more simple.
            if i >= (data_len - 1):
                i -= data_len
            if aux[i] == TREE:
                trees += 1
        return trees
