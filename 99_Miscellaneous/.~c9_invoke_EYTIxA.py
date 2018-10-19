def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


# Sample list and calls to both search and search3 with different lists
# to match conditions in above possible answers

# Search for a number in list
print(modSwapSort([20000, 5000, 2500, 100, 75, 27, 23, 4]))
