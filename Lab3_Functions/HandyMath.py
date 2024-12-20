def midpoint(num1, num2): 
    return (num1 + num2) / 2 
 
def squareroot(n): 
    return n ** 0.5 
 
def exponent(base, exp): 
    return base ** exp 

def max(num1, num2): 
# Uses a conditional statement to return the larger of num1 and num2 
    return num1 if num1 > num2 else num2 
 
print(max(20, 30)) 
print(max(25, 15)) 

def min(num1, num2): 
# Uses a conditional statement to return the smaller value of num1 and num2 
    return num1 if num1 < num2 else num2 
 
print(min(20, 30)) 
print(min(25, 15)) 