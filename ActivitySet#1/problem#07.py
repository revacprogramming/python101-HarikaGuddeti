# Strings

str = "X-DSPAM-Confidence:    0.8475"
position=str.find(":")   #to find colon position
piece=str[position+1:]   #slicing
x=float(piece)           
print(x)

#+1 to reduce blank space and remove colon
