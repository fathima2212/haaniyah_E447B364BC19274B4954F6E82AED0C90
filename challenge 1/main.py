def fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * fact(n-1)
num = int(input("enter number:"))
if(num < 0):
  print("factorial doesn't exist for negative number")
else:
  print("factorial is:",fact(num))
  
  
