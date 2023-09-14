# 271. Encode and Decode Strings
from typing import List


class Codec:
    delimiter = 'C'

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        return ''.join(f"{len(s)}{Codec.delimiter}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        length = ''
        passed_delimiter = False
        working_string = ''
        res = []

        for c in s:
            if c == Codec.delimiter and not passed_delimiter:
                length = int(length)

                # empty string case
                if length == 0:
                    res.append('')
                    length = ''
                else:
                    passed_delimiter = True

                continue

            if not passed_delimiter:
                length += c
                continue

            if passed_delimiter and length > 0:
                working_string += c
                length -= 1

                # for when using up last char in a string
                if length == 0:
                    res.append(working_string)
                    working_string = ''
                    length = '0'
                    passed_delimiter = False

                continue

        return res


c = Codec()
c.decode(c.encode(['xRkC']))
c.decode(c.encode(['del', 'del', '', 'cheeeps!']))
