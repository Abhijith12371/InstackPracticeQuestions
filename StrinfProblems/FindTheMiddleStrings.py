# Type your code here
n=input()
if len(n)>=7 and len(n)%2!=0:
  mid=len(n)//2
  print(n[mid-1:mid+2])
else:
  print(n)