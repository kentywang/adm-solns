class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        length = 0

        while i < len(word) and j < len(abbr):
            # check both are letters
            if abbr[j].isalpha():
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                    continue
                else:
                    return False  # mismatching letters

            # abbr char is not equal to word char, so it must be number
            # make sure we stop when j out of bounds or when abbr[j] is a letter again
            length = 0
            while j < len(abbr) and not abbr[j].isdigit():
                length = length * 10 + int(abbr[j])

                # invalidate if ever just zero
                if length == 0:
                    return False
                j += 1

            # trying to use up the most recent abbreviation length
            while i < len(word) and length > 0:
                i += 1
                length -= 1

        # surplus length, so didn't match length of word
        if length:
            return False

        return i == len(word) and j == len(abbr)

    """
    22:48 - 23:16 (28m; trial and error, with optimization from online soln)

    apple
         ^
    5
    ^
    """

    def validWordAbbreviation2(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                digit = 0
                # parse number
                while j < len(abbr) and abbr[j].isdigit():
                    digit = digit * 10 + int(abbr[j])
                    j += 1
                # apply number
                i += digit
            else:
                return False

        return i == len(word) and j == len(abbr)


print(Solution().validWordAbbreviation2('internationalization', 'i5a11o1'))
print(Solution().validWordAbbreviation2('a', '2'))
