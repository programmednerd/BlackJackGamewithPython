#import art

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - substract, multiply, & divide

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", & "/"

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary Operations to perform the calculations. Multiple 4 * 8 using the dic
#See below!!

def calculator():
    # print(art.logo)
    should_accumulate = True
    #ex. 1 - Program asks the user to type the first number
    num1 = float(input("What is the first number?: "))        #to be able to make the calculations, we need int or float!!

    while should_accumulate:
        for symbol in operations:        #to display the symbols as a choice
            print(symbol)

    #ex. 2 - Program asks the user to type a mathematical operator (a choice of "+", "-", "*", & "/")
        operation_symbol = input("Pick an operation: ")

    #ex. 3 - Program asks the user to type the second number
        num2 = float(input("What is the next number?: "))

    #ex. 4 - Program works out the result based on the chosne mathematical operator
    #print(f"{operations[operation_symbol](num1, num2)}")
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

    #ex. 5 - Program asks if the user wants to continue working with the previous result
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")

        #ex. 6 - If yes, program loops to use the previous result as the first number and then repeats the calculation process.
        if choice == 'y':
            num1 = answer
        # ex. 7 - If no, program asks the user for the first number again 
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()             # it will keep repeating the whole process over & over again


calculator()
