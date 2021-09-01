#Calculator using python

def add(n1,n2):
 return n1 + n2
def sub(n1,n2):
 return n1 - n2
def multiply(n1,n2):
 return n1 * n2
def divide(n1,n2):
 return n1 / n2
operations = {"+":add, "-":sub, "*":multiply, "/":divide}

num1= float(input("What's the first number?:"))
for symbol in operations:
 print(symbol)
operation_symbol = input("Pick an operations from the line above:\n")
num2 = float(input("What's the second number?:"))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
print(f"{num1}{operation_symbol}{num2}:{answer}")