from operators import *

def problem_zero(number):
    """ SC x2 binary """
    memory_zero = 0
    input = int_to_list(number)
    input.append(0)
    output = []

    for digit in input:
        output.append(memory_zero)
        memory_zero = digit

    return list_to_int(output)


# print(problem_zero(1010) == 10100)
# print(problem_zero(1011) == 10110)


def problem_one(number):
    """ SC +1 binary """
    memory_zero = 0
    input = int_to_list(number)
    input.append(0)
    input.append(0)
    input.append(0)
    output = []

    for digit in input:
        print("inputs -----")
        print(f"input: {digit}")
        print(f"memory: {not_gate(memory_zero)}")
        print(f"carry: {half_adder(digit, not_gate(memory_zero))['carry']}")
        print(f"sum: {half_adder(digit, not_gate(memory_zero))['sum']}")
        output.append(half_adder(digit, not_gate(memory_zero))['sum'])
        carry =
        memory_zero = not_gate(half_adder(digit, not_gate(memory_zero))['carry'])

        print("outputs -----")

        print(f"memory: {memory_zero}")




    return list_to_int(output)


# print(problem_one(1010) == 1011)
# print(problem_one(1011) == 1100)
print(problem_one(1011))
