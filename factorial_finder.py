i=1
n=int(input("enter the number: "))

while (n==0 or n==1):
    print(f"Factorial of {n} is 1")
    break

while (n>=1):
    i=n*i
    n=n-1

print(f"The Factorial is {i}")