# Type your code
s1=input()
s2=input()

def check(s1,s2):
  for i in s1:
    if i not in s2:
      return False
  return True
print(check(s1,s2))