s=input()
char=""
output=""
for i in s:
    if i.isalpha():
        char=i
    elif i.isdigit():
        output=output+char*int(i)
print(output)