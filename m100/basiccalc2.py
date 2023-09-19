"""
Planning
9:48 - 9:58 (10m)
??? - ??? (10m)
17:35 - ??? (3m)
19:42 - 20:01 (19m)
20:01 - 20:38 for tokenizer (37m)
20:38 - 21:19 for rest (41m)
----------------------------
Total: 120m

Observations:
- if we had already parsed the symbols, we could have a list or some other structure to represent the operators and operands
- we need to apply * / over + -
- could use stack, throw each number and op on stack and only process
- it would be useful to have a function to consume the next symbol. And a function to peek at the next symbol.
- after each number, we can either have +-, */, or EOF
- after a +- or */, we always have a number
    - when we see a */, we can immediately apply the previous number and the next number, and put it in its place
    - when we see a +-, we can't apply until we know the symbol after the 2nd operand.

Cases:
    3+5/2   => 5
    3*5-2   => 13
    5 * 5 + 5 / 5 - 5 => 19

    (5 * 5) + (5 / 5) - 5

- number    :: put on stack
- */        :: consume next number, apply op with number and stack number, push to stack
- -+        :: if operator stack nonempty, consume stack operators and and stack operands to lower t
               the stack (since commutative),
               in any case, push op to stack it and next number

Time: O(n)
Space: O(1)
"""


class Solution:
    def calculate(self, s: str) -> int:
        def tokengen(expr):
            i = 0
            val = None

            while i < len(expr):
                if expr[i].isnumeric():
                    if val is None:
                        val = 0
                    val = val * 10 + int(expr[i])

                elif expr[i] == " ":
                    if val is not None:
                        yield val
                        val = None

                else:  # expr[i] is in '*/-+'
                    if val is not None:
                        yield val
                        val = None
                    yield expr[i]

                i += 1

            if val is not None:
                yield val

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b
        }

        operators = []  # max length one, + or -
        operands = []  # max length 2

        tokeniter = tokengen(s)
        for t in tokeniter:
            if type(t) == int:
                # only handled here if previous token was a +- or this is the start
                operands.append(t)
            elif t in '+-':
                if operators:
                    # apply what's currently on the stack first
                    b = operands.pop()
                    a = operands.pop()
                    tmp = ops[operators.pop()](a, b)
                    # add result back to stack
                    operands.append(tmp)
                # add op to stack
                operators.append(t)
            else:  # / or *
                tmp = ops[t](operands.pop(), next(tokeniter))
                operands.append(tmp)

        if operators:
            b = operands.pop()
            a = operands.pop()
            tmp = ops[operators.pop()](a, b)
            operands.append(tmp)
        return operands[0]
