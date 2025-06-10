import sys

if len(sys.argv) != 4:
    print("Usage: python calc.py <num1> <operator> <num2>")
    sys.exit()



if sys.argv[2] == '+':
    print("Result:", float(sys.argv[1]) + float(sys.argv[3]))
elif sys.argv[2] == '-':
    print("Result:", float(sys.argv[1]) - float(sys.argv[3]))
elif sys.argv[2] == '*':
    print("Result:", float(sys.argv[1]) * float(sys.argv[3]))
elif sys.argv[2] == '/':
    if float(sys.argv[3]) == 0:
        print("Error: Division by zero")
    else:
        print("Result:", float(sys.argv[1]) / float(sys.argv[3]))
else:
    print("Invalid operator. Use +, -, * or /")
