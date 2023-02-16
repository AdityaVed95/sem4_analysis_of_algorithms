import random


class BinarySearchTester:

    def __int__(self):
        pass

    def binary_search_using_recursive_approach(self, list1: list, key: int, imin: int, imax: int) -> int:
        if imax < imin:
            return -1

        else:
            imid = (imin + imax) // 2

        if list1[imid] < key:
            return self.binary_search_using_recursive_approach(list1, key, imid + 1, imax)

        elif list1[imid] > key:
            return self.binary_search_using_recursive_approach(list1, key, imin, imid - 1)

        else:
            return imid

    # static method :
    def binary_search_using_iterative_approach(self, list1: list, key: int, imin: int, imax: int) -> int:
        while imax > imin:
            imid = (imax + imin) // 2
            if list1[imid] == key:
                return imid

            elif list1[imid] < key:
                imin = imid + 1

            else:
                imax = imid - 1

        return -1

    # static method :
    def create_list(self, size_of_list: int) -> list:
        list1 = []
        i = 0
        while i < size_of_list:
            list1.append(random.randint(0, 10000))
            i += 1

        return list1

    # static method :
    def sort_list(self, list1: list) -> list:
        for i in range(1, len(list1)):
            key = list1[i]
            j = i - 1
            while j >= 0 and key < list1[j]:
                list1[j + 1] = list1[j]
                j -= 1

            list1[j + 1] = key

        return list1
