# Type your code
product=1
n=int(input())
if n<0:
  print(-1)
elif n==0:
  print(0)
elif(n>=1):
  for i in range(1,n+1):
    product=product*i
  print(product)