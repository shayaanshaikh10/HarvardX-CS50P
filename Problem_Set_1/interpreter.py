exp=input("enter the expression: ")
x,y,z=exp.split(" ")
x=float(x)
z=float(z)

if y=="+":
    ans=round(float(x+z),1)
    print(ans)
elif y=="-":
    ans=round(float(x-z),1)
    print(ans)
elif y=="*":
    ans=round(float(x*z),1)
    print(ans)
elif y=="/":
    ans=round(float(x/z),1)
    print(ans)
else:
    print("enter correct exp")