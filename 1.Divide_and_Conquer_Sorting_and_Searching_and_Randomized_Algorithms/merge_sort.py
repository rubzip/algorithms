def split(x: list):
    n = len(x) // 2
    return x[:n], x[n:]


def merge(x: list, y: list) -> list:
    z = list()
    lx, ly = len(x), len(y)
    i, j = 0, 0
    while i < lx or j < ly:
        if i == lx:
            # If x is completely inserted, I insert all remaining values from y
            z += y[j:]
            j = ly
        elif j == ly:
            # If y is completely inserted, I insert all remaining values from x
            z += x[i:]
            i = lx
        elif x[i] < y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z


def merge_sort(x: list) -> list:
    if len(x) == 1:
        return x
    elif len(x) == 2:
        if x[0] > x[1]:
            return [x[1], x[0]]
        else:
            return x
    else:
        y, z = split(x)
        y_s, z_s = merge_sort(y), merge_sort(z)
        return merge(y_s, z_s)
