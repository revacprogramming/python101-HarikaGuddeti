# Functions







def computepay(hrs,rphrs):
  if hrs>40:
     pay=(hrs-40)*rphrs*1.5+40*rphrs
  else:
    pay=hrs*rphrs
  return pay
  
def main():
 hrs=input("enter hours")
 hr=float(hrs)
 rphrs=input("enter rate per hour")
 rphr=float(rphrs)
 p=computepay(hr,rphr)
 print("pay",p)

main()
