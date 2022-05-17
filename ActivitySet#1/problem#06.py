# Loops & Iterators

largest = None
smallest = None
while True:
  num=input("enter the value of number")
  if num=="done":
    break
  try:
    n=int(num)
    if largest is None:
      largest=n
    elif largest<n:
      largest=n
    if smallest is None:
      smallest=n
    elif smallest>n:
      smallest=n

  except:
    print("Invalid input")
    continue

print("maximum is",largest)
print("minimum is",smallest)

      
   
    