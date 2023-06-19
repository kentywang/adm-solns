def pangrams(s):
    seen = set()
    for char in s:
        if char != ' ':
            lowchar = char.lower()
            seen.add(lowchar)
    return 'pangram' if len(seen) == 26 else 'not pangram'
