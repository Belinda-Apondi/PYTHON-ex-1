print("Here is a simpled calculator..")
first = float(input("Enter a digit..\n"))
operator = input("type any operator i.e +, -, %, *, / \n")
second = float(input("Enter another digit...\n"))

if operator == "+" :
    answer = first + second
    print(f"the result is {answer}")

elif operator == "-" :
    answer = first - second
    print(f"the result is {answer}")

elif operator == "%" :
    answer = first % second
    print(f"the result is {answer}")

elif operator == "*" :
    answer = first * second
    print(f"the result is {answer}")

elif operator == "/" :
    answer = first / second
    print(f"the result is {answer}")

else:
    print("incorrect operator.Kindly type the right operator🤩")