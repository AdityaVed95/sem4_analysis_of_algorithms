# iterative approach

list1 = [11, 12, 22, 25, 64]

imax = len(list1) - 1
imin = 0
key = 25
imid = 0

while (imax > imin):
    imid = (imax + imin) // 2
    if list1[imid] == key:
        print("Key found at : ", imid)
        break

    elif list1[imid] < key:
        imin = imid + 1

    else:
        imax = imid - 1

print("Key NOT FOUND !!!!!!!")


def binary_search_using_iterative_approach(list1: list, key: int, imin: int, imax: int) -> int:
    while (imax > imin):
        imid = (imax + imin) // 2
        if list1[imid] == key:
            return imid

        elif list1[imid] < key:
            imin = imid + 1

        else:
            imax = imid - 1

    return -1
