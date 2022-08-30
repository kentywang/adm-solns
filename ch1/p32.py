def intdiv(a, b):
    a_neg, b_neg = (a < 0, b < 0)

    # absolute a and b
    if a_neg:
        a = a - a - a
    if b_neg:
        b = b - b - b

    q = 0

    if a_neg == b_neg:
        # Same signs
        while a >= b:
            a -= b
            q += 1
    else:
        while a > 0:
            a -= b
            q -= 1

    return q
