def factorial(a):
    if a < 1 :
        return 1
    else:
        return a * (factorial(a-1))
b=int(input("Enter a number:"))
c= factorial(b)
print('Factorial of ' + str(b) +' is: '+ str(c))