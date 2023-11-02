#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the number of command-line arguments
    num_args = len(sys.argv) - 1

    # Check if the correct number of arguments is provided
    if num_args != 3:
        print("Usage: ./my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get the operator and check if it's valid
    operator = sys.argv[2]
    valid_operators = ['+', '-', '*', '/']
    if operator not in valid_operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    # Import functions for the supported operations
    from calculator_1 import add, sub, mul, div

    # Get the operands from the command-line arguments
    operand_a = int(sys.argv[1])
    operand_b = int(sys.argv[3])

    # Perform the operation based on the operator
    if operator == '+':
        result = add(operand_a, operand_b)
    elif operator == '-':
        result = sub(operand_a, operand_b)
    elif operator == '*':
        result = mul(operand_a, operand_b)
    else:
        result = div(operand_a, operand_b)

    # Print the result of the operation
    print(f"{operand_a} {operator} {operand_b} = {result}")
