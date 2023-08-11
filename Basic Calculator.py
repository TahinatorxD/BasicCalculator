num1 = int(input("Enter your First number: "))
num2 = int(input("Enter your Second number: "))
calculation = input("Enter the Arithmetic Operator (+,-,*,/): ")
if calculation == "+" :
    result = num1 + num2
elif calculation == "-" :
    result = num1 - num2
elif calculation == "/" :
    result = num1 / num2
elif calculation == "*" :
    result = num1 * num2
else:
    print("The Operator you entered is illegal")

print(result)