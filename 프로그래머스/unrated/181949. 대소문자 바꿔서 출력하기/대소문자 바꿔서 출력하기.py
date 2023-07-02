str = input()

alpha = ""
for i in str:
    if i.isupper():
        alpha += i.lower()
    else:
        alpha += i.upper()
    
print(alpha)