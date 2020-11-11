# 1. We are going some inputs where it will ask them if they want * or / or + * XXX
#2. We are going to have an if statement where if will check for +,-,*,/ XXX
#3. We are going to ask for 2 numbers.
#4. We are going to have a try statement we are going to check if they put spaces/letters etc.
def which_sing_func():
    global which_sing
    which_sing = input('''
    Hello, I am the calculator of the future. What do you want
    a add(+)
    b substraction(-)
    c multiplication(*)
    d divison(/)
    e Quit the program
    :  
    ''')
which_sing_func()


#Add


if which_sing == "a" or which_sing == "add" or which_sing == "Add"or which_sing == "+" or  which_sing == "addition" or which_sing == "Addition":
    def addition_func():
        try:
            number1 = int(input("Enter your first number:  "))
            number2 = int(input("Enter your second number:  "))
            # Way 1
            addition = number1 + number2
            print("The answer is ", addition)
            # Way 2
            print("The answer is ", number1 + number2)
            def try_again_func():
                global try_again
                try_again = input("Do you want to try again Yes(y) and any other key for no: ")
            try_again_func()
            if try_again == "y" or try_again == "Y" or try_again == "yes" or try_again == "Yes":
                addition_func()
            else:
                which_sing_func()
        except ValueError:
            print("Only allow numbers")
            addition_func()
    addition_func()




#Substract




elif which_sing == "b" or which_sing == "substraction" or which_sing == "Substraction"or which_sing == "-" or  which_sing == "minus" or which_sing == "Minus" :
    def subtraction_func():
        try:
            number1 = int(input("Enter your first number:  "))
            number2 = int(input("Enter your second number:  "))
            # Way 1
            subtraction = number1 - number2
            print("The answer is ", subtraction)
            # Way 2
            print("The answer is ", number1 - number2)
            def try_again_func():
                global try_again
                try_again = input("Do you want to try again Yes(y) and any other key for no: ")
            try_again_func()
            if try_again == "y" or try_again == "Y" or try_again == "yes" or try_again == "Yes":
                subtraction_func()
            else:
                which_sing_func()
        except ValueError:
            print("Only allow numbers")
            subtraction_func()
    subtraction_func()





#Multiply



elif which_sing == "c" or which_sing == "multiplication" or which_sing == "Multiplication"or which_sing == "*" or  which_sing == "multiply" or which_sing == "Multiply" :
    def multiplication_func():
        try:
            number1 = int(input("Enter your first number:  "))
            number2 = int(input("Enter your second number:  "))
            # Way 1
            multiplication = number1 * number2
            print("The answer is ", multiplication)
            # Way 2
            print("The answer is ", number1 * number2)
            def try_again_func():
                global try_again
                try_again = input("Do you want to try again Yes(y) and any other key for no: ")
            try_again_func()
            if try_again == "y" or try_again == "Y" or try_again == "yes" or try_again == "Yes":
                multiplication_func()
            else:
                which_sing_func()
        except ValueError:
            print("Only allow numbers")
            multiplication_func()
    multiplication_func()




#Divide




elif which_sing == "d" or which_sing == "divison" or which_sing == "Divison"or which_sing == "/" or  which_sing == "divide" or which_sing == "Divide":
    def division_func():
        try:
            number1 = int(input("Enter your first number:  "))
            number2 = int(input("Enter your second number:  "))
            # Way 1
            division = number1 / number2
            print("The answer is ", division)
            # Way 2
            print("The answer is ", number1 / number2)
            def try_again_func():
                global try_again
                try_again = input("Do you want to try again Yes(y) and any other key for no: ")
            try_again_func()
            if try_again == "y" or try_again == "Y" or try_again == "yes" or try_again == "Yes":
                division_func()
            else:
                which_sing_func()
        except ValueError:
            print("Only allow numbers")
            division_func()
    division_func()


elif which_sing == "e" or which_sing == "E" or which_sing == "Exit" or which_sing == "exit":
    print("Good bye")
else:
    print("I did not understand you.")
    which_sing_func()