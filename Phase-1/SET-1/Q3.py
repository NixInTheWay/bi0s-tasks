string = input("enter a string: ")
new_string = ""
for char in string:
    if char.isupper():
        start = ord('A')
    elif char.islower():
        start = ord('a')
    else:
        new_string = new_string + char
        continue
    new_char = chr(start + (ord(char) - start + 2) % 26 )
    new_string = new_string + new_char
print(new_string)
    
        
