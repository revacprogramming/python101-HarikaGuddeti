score=input("enter score:")
s=float(score)
x='error'
if s>=0.9:
  x='A'
elif s>=0.8:
  x='B'
elif s>=0.7:
  x='c'
elif s>=0.6:
  x='D'
elif s<0.6:
  x='F'
print(x)

#conditional execution 