s=input()
prev=s[0]
c=1
sr=""
i=1
while i<len(s):
    if s[i]==prev:
        c+=1
        # i+=1
    else:
        sr+=prev+str(c)
        prev=s[i]
        c=1
    i+=1
sr+=prev+str(c)
print(sr)