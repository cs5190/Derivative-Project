import inspect
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getDerivative(expressionression):
    #this can be our main recursive function

    #simply show how to write lambdas in python and pass values
    #clearly for this derivative function we need no values to pass
    #this must parse the lambda expressionression and then handle it in chunk


    return expressionression

def monos(expression):
    #read string for + or -
        #every + or - append next mono to list


    list = ["x", "x^2", "x^3"]
    return list

#version 0.1
def power(expression):
    #note needs implementation for fractions ,negative exponents and expressions as exponents
    #only works for whole number coefficients and exponents

    coefficient = 0
    variable = "x"
    exponent = 1
    indexVar = 0
    indexExp = 0

    if expression[0] == "0":
        return 0

    for character in expression:
        if isLetter(character):
            break
        if indexVar == len(expression) - 1:
            return 0
        indexVar += 1

    coefficient = expression[0:indexVar]
    variable = expression[indexVar]

    indexExp = indexVar+2

    if expression[indexVar+1] == '^':
        for character in expression[indexExp:]:
            if isLetter(character):
                break
            indexExp += 1
    exponent = expression[indexVar+2:indexExp]

    newCoefficient = int(coefficient) * int(exponent)
    newExponent = int(exponent) - 1

    return str(newCoefficient) + str(variable) + "^" + str(newExponent)



def isLetter(char):
    return not char.isdigit()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expression = "3x^3"

    print(power(expression))

    #getDerivative(expression)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
