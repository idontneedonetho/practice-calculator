#V1
while True:
    
    number1 = input("Number: ")
    sign = input("Operation: ")
    number2 = input("Number: ")
    if sign == ("+"):
        print(float(number1) + float(number2))
        break
    elif sign == ("-"):
        print(float(number1) - float(number2))
        break
    elif sign == ("x"):
        print(float(number1) * float(number2))
        break
    elif sign == ("/"):
        print(float(number1) / float(number2))
        break
    else:
        print("Try +, -, x, /")
        continue