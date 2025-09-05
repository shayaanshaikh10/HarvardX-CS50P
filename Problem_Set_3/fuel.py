def main():
    x=get_frac()
    x=round(x)
    if(x<=1):
        print("E")
    elif(x>=99):
        print("F")
    else:
        print(f"{x}%")

def get_frac():
    while(True):
        try:
            str=input("enter:")
            x,y=str.split("/")
            x=int(x)
            y=int(y)
            if(x>y):
                continue
            if(x<0 or y<0):
                continue
            percentage=(x/y)*100
        except:
            continue
        else:
            break
    return percentage


main()