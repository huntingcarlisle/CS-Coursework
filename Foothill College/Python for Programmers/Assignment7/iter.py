listExample = [1, 2, 3, 4, 5]


def sumList(listToAdd):
    if (len(listToAdd) == 0):
        return 0
    else:
        i = iter(listToAdd)
        return next(i) + sumList(list(i))

print(sumList(listExample))

## ===== OUTPUT ======
# ~/workspace/CS-Coursework/Foothill College/Python for Programmers/Assignment7/ (master) $ python iter.py
# 15


