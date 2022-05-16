# Conditional Execution
hrs = float(input("enter hours:"))
rate = float(input("enter rate:"))
gross = (hrs * rate) 
if hrs <=40:
  gross=hrs*rate
else:
  gross=40 * rate + 1.5 * rate *(hrs - 40)
print(gross)
