n=int(input())
upper_case=0
lower_case=0
digit=0
for i in n:
  if(i.isupper()):
    upper_case+=1
  elif(i.islower()):
    lower_case+=1
  elif(i.isdigit()):
    digit+=1