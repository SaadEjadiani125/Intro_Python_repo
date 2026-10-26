a = float(input("First number: "))
op = input("Operator (+ - * /): ")
b = float(input("Second number: "))
 
if op == "+":
    print(f"{a} {op} {b} = {a+b}")
elif op == "-":
    print(f"{a} {op} {b} = {a-b}")
elif op == "*":
    print(f"{a} {op} {b} = {a+b}")
elif op == "/":
    if b != 0:
        print(f"{a} {op} {b} = {a/b}")
    else:
        print("Error: you tried dividing by 0")
else:
    print("Please enter a valid op")