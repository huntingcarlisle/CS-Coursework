def and_gate(zero, one):
    return int(zero and one)
# and_gate tests
# print(and_gate(0,0))
# print(and_gate(0,1))
# print(and_gate(1,0))
# print(and_gate(1,1))

def or_gate(zero, one):
    return int(zero or one)
# or_gate tests
# print(or_gate(0,0))
# print(or_gate(0,1))
# print(or_gate(1,0))
# print(or_gate(1,1))

def not_gate(zero):
    return int(not(zero))
# not_gate tests
# print(not_gate(0))
# print(not_gate(1))


def xor_gate(zero, one):
    return and_gate(or_gate(zero, one), not_gate(and_gate(zero, one)))
    # return int((zero or one) and not(zero and one))
# xor_gate Tests
# print(xor_gate(0,0))
# print(xor_gate(0,1))
# print(xor_gate(1,0))
# print(xor_gate(1,1))


def half_adder(zero, one):
    return {'carry': and_gate(zero, one), 'sum': xor_gate(zero, one)}
# half_adder tests
# print(half_adder(0, 0))
# print(half_adder(0, 1))
# print(half_adder(1, 0))
# print(half_adder(1, 1))


# NUMBER OPERATORS
def dec_to_bin(x):
    return int(bin(x)[2:])


def bin_to_dec(x):
    return int(str(x), 2)


def int_to_list(x):
    my_list = list(str(x))
    my_list.reverse()
    return my_list


def list_to_int(x):
    x.reverse()
    return int(''.join(str(i) for i in x))


# test
# print(dec_to_bin(21))
#
# print(bin_to_dec(1011))
#
# print(int_to_list(123))
#
# print(list_to_int(['1', '4', '5']))
