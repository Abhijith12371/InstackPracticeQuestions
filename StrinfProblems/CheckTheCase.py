import re
n=input()

count=re.findall("USA",n,re.IGNORECASE)
print(len(count))