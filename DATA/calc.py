
num1 = float(input("enter first number: "))
op = raw_input("enter operator: ")
num2 = float(input("enter second number"))

if op == "+":
    print("Ans [ " + num1 + num2 + " ]")
elif op == "-":
    print("Ans [ " + num1 - num2 + " ]")
elif op == "*":
    print("Ans [ " + num1 * num2 + " ]")
elif op == "/":
    print("Ans [ " + num1 / num2 + " ]")
else:
    print("syntax error!!!")
