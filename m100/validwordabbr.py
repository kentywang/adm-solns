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


print(Solution().validWordAbbreviation('internationalization', 'i12iz4n'))
