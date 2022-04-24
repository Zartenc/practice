import re


class LetterCombination():
    def input_digit(self, digit):
        self.digit = str(digit)
        if re.fullmatch("[1-9][0-9]?|[0]", self.digit) is None:
            print("Input:{0} is wrong. Support converting the digits from 0 to 99!".format(self.digit))
            return

        letters = self.letter_combinations(self.digit)
        print("Input:{0}  output:{1}".format(self.digit, letters))

    def letter_combinations(self, digit):
        dic = {0: [''],
               1: [''],
               2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z']
               }

        ret = []

        if len(digit) == 1:
            return dic[int(digit[0])]

        result = self.letter_combinations(digit[1:])

        for i in dic[int(digit[0])]:
            for j in result:
                ret.append(i + j)
        return ret


if __name__ == '__main__':
    letter = LetterCombination()
    letter.input_digit(23)
    letter.input_digit(9)
    letter.input_digit(99)
    letter.input_digit(100)
