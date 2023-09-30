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

#
# class Solution:
#     def calculate(self, s: str) -> int:
#         def tokengen(expr):
#             i = 0
#             val = None
#
#             while i < len(expr):
#                 if expr[i].isnumeric():
#                     if val is None:
#                         val = 0
#                     val = val * 10 + int(expr[i])
#
#                 elif expr[i] == " ":
#                     if val is not None:
#                         yield val
#                         val = None
#
#                 else:  # expr[i] is in '*/-+'
#                     if val is not None:
#                         yield val
#                         val = None
#                     yield expr[i]
#
#                 i += 1
#
#             if val is not None:
#                 yield val
#
#         ops = {
#             '+': lambda a, b: a + b,
#             '-': lambda a, b: a - b,
#             '*': lambda a, b: a * b,
#             '/': lambda a, b: a // b
#         }
#
#         operators = []  # max length one, + or -
#         operands = []  # max length 2
#
#         tokeniter = tokengen(s)
#         for t in tokeniter:
#             if type(t) == int:
#                 # only handled here if previous token was a +- or this is the start
#                 operands.append(t)
#             elif t in '+-':
#                 if operators:
#                     # apply what's currently on the stack first
#                     b = operands.pop()
#                     a = operands.pop()
#                     tmp = ops[operators.pop()](a, b)
#                     # add result back to stack
#                     operands.append(tmp)
#                 # add op to stack
#                 operators.append(t)
#             else:  # / or *
#                 tmp = ops[t](operands.pop(), next(tokeniter))
#                 operands.append(tmp)
#
#         if operators:
#             b = operands.pop()
#             a = operands.pop()
#             tmp = ops[operators.pop()](a, b)
#             operands.append(tmp)
#         return operands[0]

"""
10:14 - 11:12 (58m)


Cases:
3 + 2 * 2
3 + 2
- when see * or /, apply them immediately
- when see + or -, save first operand & operator
    - if there's already a saved operand and operator, apply the saved, then save the new 
    - this will keep our stack O(1)
- after traversed full expression, apply leftover stack
"""


class Solution:
    def calculate(self, s: str) -> int:
        def tokenize(expr):
            i = 0
            while i < len(expr):
                if s[i].isdigit():
                    acc = 0
                    while i < len(expr) and s[i].isdigit():
                        acc = acc * 10 + int(s[i])
                        i += 1
                    yield acc
                elif s[i] != ' ':
                    yield s[i]
                    i += 1
                else:
                    i += 1

        saved = []
        plusminus = []

        tokens = tokenize(s)

        for t in tokens:
            if type(t) == int:
                saved.append(t)
            else:
                # operator, so we'll def have another token after (2nd operand)
                operand2 = next(tokens)
                if t == '*':
                    saved[-1] *= operand2
                elif t == '/':
                    saved[-1] //= operand2
                elif t == '+' or t == '-':
                    if plusminus:
                        # process the previous plus/minus op to avoid building up stack
                        saved[0] = plusminus.pop()(saved[0], saved.pop())
                    saved.append(operand2)
                    if t == '+':
                        plusminus.append(lambda x, y: x + y)
                    else:
                        plusminus.append(lambda x, y: x - y)

        if plusminus:
            return plusminus[0](saved[0], saved[1])

        return saved[0]


"""
Online soln. Pretty elegant, but I don't think it's intuitive and derivable in 20m.
"""


class Solution:
    def calculate(self, s: str) -> int:
        curr_res = 0
        res = 0
        num = 0
        op = "+"  # keep the last operator we have seen

        # append a "+" sign at the end because we can catch the very last item
        for ch in s + "+":
            if ch.isdigit():
                num = 10 * num + int(ch)

            # if we have a symbol, we would start to calculate the previous part.
            # note that we have to catch the last chracter since there will no sign afterwards to trigger calculation
            if ch in ("+", "-", "*", "/"):
                if op == "+":
                    curr_res += num
                elif op == "-":
                    curr_res -= num
                elif op == "*":
                    curr_res *= num
                elif op == "/":
                    # in python if there is a negative number, we should alway use int() instead of //
                    curr_res = int(curr_res / num)

                # if the chracter is "+" or "-", we do not need to worry about
                # the priority so that we can add the curr_res to the eventual res
                if ch in ("+", "-"):
                    res += curr_res
                    curr_res = 0

                op = ch
                num = 0

        return res


print(Solution().calculate("1-2*3"))
