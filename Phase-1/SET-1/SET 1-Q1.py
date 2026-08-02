#Write a Python Program to input and decode the following ternary numeric notations
Encrypted = input("Enter notation: ")
Decoded = ""
i=0
while i>len(Encrypted):
  if Encrypted[i]+Encrypted[i+1] == "xx":
    Decoded =+ "00"
    i =+ 2
  elif Encrypted[i]+Encrypted[i+1] == "ox":
    Decoded =+ "1"
    i =+ 2
  elif Encrypted[i]+Encrypted[i+1] == "oo":
    Decoded =+ "2"
    i =+ 2
  elif Encrypted[i]+Encrypted[i+1] == "xo":
    i =+ 1
    Decoded =+ "1"
print(Decoded)
  
