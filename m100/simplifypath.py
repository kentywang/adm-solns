"""
Planning:       7:43 - 8:17 (34min)
Coding lexer:         8:46 - 9:00 (14min)
Coding parser:         19:01 - 19:12, 20:10-20:25 (11+15)

-----------------------------

Observations:
-----------------------------
- we want to specifically handle differently single period, double period, and any sequence of slashes.
- everything else will be treated as a dirname
- we can specifcally tokenize our input into these 4 types (since we're typing them, we're actually building a lexer)
a-z _   |  .  | .. |  /
- slash type can be tokenize any number of adjacent slashes into 1
- we then build a try building a tree/LL
- always keep a ref to the root for ".."
- no need to keep the branches though. Just update the .next of prev node with new node.
- parse tokens into a path of nodes, each node is a dir.
    - this needs to be finished first before we can start on the next step, otherwise we'll possibly backtrack, which is a no-no in the canonical syntax
- traverse the tree until we stop iterating, building up the string as we traverse.
    - every node we traverse, add a slash

5 cases:
-----------------------------
/abc/           => /abc
/...            => /...
/foo/./abc      => /foo/abc
/foo/../abc     => /abc
/foo//abc       => /foo/abc

Option
1.  /foo/../abc/     => ['foo', '..', 'abc',]    tokenizer/lexer (lazy)
2.  ['foo', '..', 'abc',] => [/, foo, .., abc]   parsed into LL of dirs, shortened
3. print

Time: O(n)
Space: O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        def lexer(p):
            i = 0

            while i < len(p):
                if p[i] == '/':
                    # store no slashes; not needed
                    while i < len(p) and p[i] == '/':
                        i += 1

                # we can treat dots the same as all other chars, since we can just read them in O(1) to
                # determine their type
                else:
                    res = []
                    while i < len(p) and p[i] != '/':
                        res.append(p[i])
                        i += 1
                    yield ''.join(res)

        def parser(tokens):
            # also shortens
            from collections import deque

            dq = deque([])  # empty means just root dir

            # start at the second token
            for dir in tokens:
                # take no action
                if dir == '.':
                    pass

                elif dir == '..':
                    if dq:
                        dq.pop()

                else:
                    dq.append(dir)

            return dq

        tokens = lexer(path)
        ll = parser(tokens)
        return '/' + '/'.join(ll)
