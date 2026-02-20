def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
num = int(input("Enter the number.."))
if num < 0:
    print ("no factorial...") 
elif num == 0:
    print ("factorialber is 1...")
else:
    print("the factorial of ", num , "is" , fact(num) )
