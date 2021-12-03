def validate_brackets(input):

    opened = ["{", "[", "("]

    closed = ["}", "]", ")"]

    bracket = []

    for i in input:

        if i in opened:

            bracket.append(i)

        elif i in closed:

            index = closed.index(i)

            if bracket and (opened[index] == bracket[len(bracket)-1]):

                bracket.pop()
            else:

                False
    if not bracket:

        return True

    else:

        return False
