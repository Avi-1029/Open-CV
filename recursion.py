#Iterative approach (loop)
n = 5
total = 0

for x in range(n+1):
    #print(x)
    total = total + x
    
print(total)

#Recursion approach (A function calling itself)


def add(a):
    if a == 1:
        return 1
    else:
        return a+add(a-1)
    
print(add(5))
    
#Fibonacci Series

def fib(f):
    if f == 0 or f == 1:
        return f
    else: 
        return fib(f-1) + fib(f-2)

print(fib(30))

#Factorial 

def fact(e):
    if e == 1:
        return 1
    else:
        return e*fact(e-1)
    
print(fact(5))