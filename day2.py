# https://adventofcode.com/2020/day/2

from pathlib import Path

FOLDER = "inputs/"
INPUT_FILE = "day2.txt"


# class functions

def get_range(char_range):
    aux = list(char_range)
    # print(aux)
    data_len = len(aux)
    dash_pos = 0
    min_num_str = ''
    min_num = 0
    max_num_str = ''
    max_num = 0

    # finding the dash position
    for i, element in enumerate(aux):
        if element == '-':
            dash_pos = i

    # getting the minimum number
    for i in range(0, dash_pos):
        min_num_str += aux[i]

    # getting the maximum number
    for i in range(dash_pos + 1, data_len):
        max_num_str += aux[i]

    # let's cast'em into int numbers
    min_num = int(min_num_str)
    max_num = int(max_num_str)

    # ...and let's put them in a list
    char_range = [min_num, max_num]

    return char_range


def get_char(char):
    # the data we care about in this function is the character that exists before the ':' symbol
    # this symbol, conveniently, is always the last element in the 'char' list

    # we also know, by inspecting the input file, that this data is 2 characters long
    # but what if we don't? let's count it anyway
    data_len = len(char)

    # let's take away the ':' symbol
    aux = ''
    for i in range(0, data_len - 1):
        aux += char[i]

    return aux


def password_is_valid(char_range, character, password):
    counter = 0

    # comparing every character with the required character and counting everytime it is present
    for element in list(password):
        if element == character:
            counter += 1

    # checking if the character appears a correct number of times, according to the range
    if char_range[0] <= counter <= char_range[1]:
        answer = True
    else:
        answer = False

    return answer


class Day2:
    def __init__(self):
        # making the file path universally compatible with pathlib
        folder = Path(FOLDER)
        file_to_open = folder / INPUT_FILE

        # input file opening and reading
        with open(file_to_open) as file:
            file_input = file.read()
            self.data = file_input.split('\n')

        print(f'Day 2, Part 1: {self.part1()}')
        print(f'Day 2, Part 2: {self.part2()}')

    def part1(self):
        """
        --- Day 2: Password Philosophy ---
        Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via
        toboggan.

        The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our
        computers; we can't log in!" You ask if you can take a look.

        Their password database seems to be a little corrupted: some passwords wouldn't have been allowed by the
        Official Toboggan Corporate Policy that was in effect when they were chosen.

        To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the
        corrupted database) and the corporate policy when that password was set.

        For example, suppose you have the following list:

        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc

        Each line gives the password policy and then the password. The password policy indicates the lowest and highest
        number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the
        password must contain 'a' at least 1 time and at most 3 times.

        In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances
        of 'b', but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within
        the limits of their respective policies.

        How many passwords are valid according to their policies?
        """

        valid_passwords = 0

        for element in self.data:
            aux = element.split()
            # now, for each element, we'll have:
            #   in aux[0] the range of times the character must appear
            #   in aux[1] the character and the symbol ':'
            #   in aux[2] the password

            char_range = get_range(aux[0])
            character = get_char(aux[1])

            if password_is_valid(char_range, character, aux[2]):
                valid_passwords += 1

        return valid_passwords

    def part2(self):

        """
        --- Part Two ---
        While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan
        Corporate Authentication System is expecting.

        The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old
        job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little
        differently.

        Each policy actually describes two positions in the password, where 1 means the first character, 2 means the
        second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
        Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant
        for the purposes of policy enforcement.

        Given the same example list from above:

        1-3 a: abcde is valid: position 1 contains a and position 3 does not.
        1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
        2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

        How many passwords are valid according to the new interpretation of the policies?
        """

        # we can use almost every part of the 'part1' method for this task

        valid_passwords = 0

        for element in self.data:
            aux = element.split()
            # now, for each element, we'll have:
            #   in aux[0] the range of times the character must appear
            #   in aux[1] the character and the symbol ':'
            #   in aux[2] the password

            # now it's not a range but a set of positions
            char_positions = get_range(aux[0])
            character = get_char(aux[1])
            password = list(aux[2])

            # print(password)

            # as the data does not accept 'index 0' we have to subtract 1 to our password list elements
            # in order to use the XOR bitwise operator, we'll have to convert every condition of if to bool
            if bool(password[char_positions[0] - 1] == character) ^ bool(password[char_positions[1] - 1] == character):
                valid_passwords += 1

        return valid_passwords
