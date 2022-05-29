import math
def rectangle(l,b):
  area=l*b
  a=float(area)
  return area
  
def main():

  p1=float(input("enter the points:",x1,y1))
  x2,y2=float(input("enter the points:"))
  x3,y3=float(input("enter the points:"))
  
  l1=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
  l2=math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
  a=rectangle(l1,l2)
  print("area",a)
main()
  

