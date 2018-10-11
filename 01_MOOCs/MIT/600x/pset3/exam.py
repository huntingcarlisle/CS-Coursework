def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def myFunction(value):
        n = 0
        for i in L:
            n = value*n + i
            print (n)
        return n
    return myFunction



print(general_poly([1, 2, 3, 4])(10))

# K = {1: 1, 2: 1, 3: 1}
# print(uniqueValues(K))
