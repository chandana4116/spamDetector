def horspool(text, pattern):
    m = len(pattern)
    n = len(text)

    shift = {}

    for k in range(m - 1):
        shift[pattern[k]] = m - 1 - k

    i = m - 1

    while i < n:
        k = 0

        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1

        if k == m:
            return True

        i += shift.get(text[i], m)

    return False