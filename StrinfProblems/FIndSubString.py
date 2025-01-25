s = "Abhijith"
sub_string = "Abhi"
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
if sub_string in l:
    print("Yes,String Found")
else:
    print("NO ,String Not Found")
    

# s = "Abhijith"
# sub_string = "Abhi"
# matches = []

# for i in range(len(s) - len(sub_string) + 1):
#     if s[i:i+len(sub_string)] == sub_string:
#         matches.append(s[i:i+len(sub_string)])  # Add the match to the list

# if matches:
#     print(f"Found matches: {matches}")
# else:
#     print(f"No matches found for '{sub_string}'")
