s=input()
#a4k3b2
#aeknbd
output=""
for i in s:
    if i.isalpha():
       output=output+i
       x=i
    elif i.isdigit():
        y=int(i)
        aci_char=ord(x)
        aci_letter=chr(aci_char+y)
        output=output+aci_letter
print(output)