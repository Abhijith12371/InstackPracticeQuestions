def fib(n):
  a=0
  b=1
  while a<=n:
    if a==n:
      return True
    a,b=b,a+b
  return False
n=int(input())
if fib(n):
  print("1")
else:
  print("0")