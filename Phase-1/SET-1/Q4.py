string = input("Enter a string: ")
dict = {}
for char in string:
    if char in dict.keys():
        values = dict[char] + 1
    else:
        values = 1
    dict[char] = values
for k,v in dict.items():
    print(k,":",v)
