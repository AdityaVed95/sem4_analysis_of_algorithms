def binary_search_using_recursive_approach(list1 : list , key : int , imin : int , imax : int) -> int:
    if imin==imax:
        if list1[imin] == key:
            return imin
        else:
            return -1

    else:
        imid = imin + imax //2

        if key == list1[imid]:
            return imid

        if key < list1[imid]:
            binary_search_using_recursive_approach(list1,key,imin,imid-1)

        elif key > list1[imid]:
            binary_search_using_recursive_approach(list1,key,imid+1,imax)


