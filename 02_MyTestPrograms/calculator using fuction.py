def sum (a,b):
    return a+b
def Subtract (a,b):
    return a-b
def Multiple (a,b):
    return a*b
def Divide (a,b):
    return a/b

calc= input("Enter Your choice +,-,*,/,\n")
x= int(input("Enter Number First\n"))
y= int(input("Enter Number Second\n"))
if (calc =='+'):
        r= sum(x,y)
elif (calc =='-'):
        r= Subtract(x,y)
elif (calc =='*'):
        r= Multiple(x,y)
elif (calc =='/'):
        r= Divide(x,y)
print("Result",r)