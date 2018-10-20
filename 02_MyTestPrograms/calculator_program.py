#Program for simple calculator
print("Press 1 to add")
print("Press 2 to Subtract")
print("Press 3 to Multiple")
print("Press 4 to Divied")

calc = input ("Enter your choice +,-,*,/")
x = int (input ("Enter your Number"))
y = int (input ("Enter your Number"))

if (calc =='1'):
    r=x+y
elif (calc =='2'):
    r=x-y
elif (calc =='3'):
    r=x*y
elif (calc =='4'):
    r=x/y
print("result:",r)
