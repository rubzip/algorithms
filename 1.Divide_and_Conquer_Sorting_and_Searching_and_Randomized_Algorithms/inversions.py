'''
Download the text file here. (Right click and save link as)
This file contains all of the 100,000 integers between 1 and
100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file
given, where the ith row of the file indicates the ith entry
of an array.

Because of the large size of this array, you should implement
the fast divide-and-conquer algorithm covered in the video
lectures. The numeric answer for the given input file should
be typed in the space below.
'''
def split(x: list):
    n = len(x) // 2
    return x[:n], x[n:]


def merge(x: list, y: list):
    z = list()
    lx, ly = len(x), len(y)
    i, j = 0, 0
    inversions = 0
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
            inversions += lx - i
    return z, inversions


def merge_and_count(x: list):
    if len(x) == 1:
        return x, 0
    elif len(x) == 2:
        if x[0] > x[1]:
            return [x[1], x[0]], 1
        else:
            return x, 0
    else:
        y, z = split(x)
        y_s, cy = merge_and_count(y)
        z_s, cz = merge_and_count(z)
        merged, c = merge(y_s, z_s)
        c_total = c + cy + cz
        return merged, c_total


with open('data.txt') as file:
    x = file.readlines()
y = list(map(lambda t: int(t.replace('\n', '')), x))
y_sorted, n_inversions = merge_and_count(y)

print(n_inversions)