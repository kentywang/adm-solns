"""
Thinking of it as numbers makes it easier. Say we look for prefix 567. We can find exactly 567
in O(lg n) time. But as a string, we need to compare each letter, so that's potentially l comparisons
per each node checked. So O(l lg n) to find 567. But then we gotta check every successor node after
567 until 567 is no longer a prefix. That's m nodes we'll traverse. In each of those, we'll need to
keep doing up to l char comparisons, so O(l lg n + ml)

Book says O(ml lg n), but I think that's only if you decide to try and find each of the m strings
from the root, and you search specifically for each of them (vs getting all the elements from when
the prefix should be to when the prefix ends).
"""
