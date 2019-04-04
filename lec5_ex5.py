def list_set(L1, L2):
    # ca trong A v
    print(set(L1) & set(L2))

    #chi co trong A
    print(set(L1) - (set(L2)))
    #chi co trong B
    print(set(L2) - (set(L1)))
    #khong co ca trong A va B
    print(set(L1) ^ set(L2))
L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]
list_set(L1, L2)