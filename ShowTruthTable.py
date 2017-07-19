""" show_truth_table.py
    Luke Griffith
    Prints truth tables for input expression via an interactive shell.
"""

import re
import string
from operator import xor

def show_truth_table(propositional_algebra, compound_proposition):
    """ 09 October 2016
        Luke Griffith
        show_truth_table()
        This function accepts an array of algebra letters, and a compound proposition as a string
        using the Python syntax, the function will output a truth table of all values and the result
        of the compound proposition.
    """
    # Argument Checking
    if not (isinstance(propositional_algebra, (list)) or  isinstance(compound_proposition, (str))):
        raise Exception("Invalid arguments.")

    num_letters = len(propositional_algebra)
    list_number_letters = list(range(0, num_letters))
    rows = 2**num_letters

    # obtaining exponents for base 2, from the number of proposition algebra letters.
    exponents = get_base_exponent(2, num_letters)

    # Obtaining count of letters.
    proposition_length = len(compound_proposition)

    # Sorting list lexiconlically.
    propositional_algebra.sort()

    table = dict()

    for letter_position in range(0, num_letters):

        letter = propositional_algebra[letter_position]
        print("|", "%-7s" % letter, end="")

        # Set initial table value to True for all letters
        table[letter] = False

        # Code executes at the last column (the expression)
        if letter_position == num_letters - 1:

            formatted_string = str("%-" + str(proposition_length) + "s")
            print("|", formatted_string % compound_proposition, "|")

    exponents.reverse()
    for row_position in range(0, rows):

        for letter_position in list_number_letters:

            letter = propositional_algebra[letter_position]
            exponent = exponents[letter_position]

            mod0 = row_position %   exponent

            if mod0 == 0:
                table[letter] = not table[letter]

            print("|", "%7s" % table[letter], end="")

            current_expression = str(letter + " = " + str(table[letter]))
            exec(current_expression)

            if letter_position == list_number_letters[-1]:
                ans = eval(compound_proposition)
                formatted_string = str("%" + str(proposition_length) + "s")
                print("|", formatted_string % ans, "|")




def get_base_exponent(base, place):
    """ 26th December 2016
        Luke Griffith
        Function returns the exponent of a given base, to the place provided
        Keyword Args:
        base - number base
        place - position to obtain exponents to
    """
    # function obtains exponents of base
    exp_range = range(0, place)
    arr = []
    for exp in exp_range:
        result = pow(base, exp)
        arr.append(result)
    return arr



def generate_algebra(expression_string):
    """ 26th December 2016
        Luke Griffith
        returns list of algebra letters from expression.
    """
    alpha = list(string.ascii_lowercase)
    exp = re.split(r" |\(|\)", expression_string)
    algebra_list = list()

    for i in range(0, len(alpha)):
        for item in exp:
            letter = alpha[i]
            if letter == item:
                algebra_list.append(letter)

    algebra_list = list(set(algebra_list))

    if len(algebra_list) == 0:
        raise LookupError('Unable to reduce expression to list.')

    return algebra_list

print()



while True:

    EXPRESSION = input("enter python expression or type exit.\n\t> ")

    if EXPRESSION != "exit":

        print()
        if not EXPRESSION == "exit":
            try:
                ALGEBRA = generate_algebra(EXPRESSION)
                show_truth_table(ALGEBRA, EXPRESSION)
                print()
            except LookupError:
                print("\n\nInvalid expression.")
    else:
        break
