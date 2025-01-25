s=input()
chars=[]
digits=[]
for i in sorted(s):
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        chars.append(i)
print("".join(digits+chars))