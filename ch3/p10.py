from util import asserter


def anagram(x: str, y: str) -> bool:
    pass


asserter(lambda: anagram('silent', 'listen'), True)
asserter(lambda: anagram('incest', 'insect'), True)
asserter(lambda: anagram('baa', 'bab'), False)
asserter(lambda: anagram('aab', 'ab'), False)
