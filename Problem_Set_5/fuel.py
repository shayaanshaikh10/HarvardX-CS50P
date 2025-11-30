def main ():
    while (True):
        try:
            fraction = input("enter:")
            percentage = convert(fraction)
        except ValueError:
            print("please enter correct fraction")
        except ZeroDivisionError:
            print("y should not be zero")
        else:
            break
    indi = gauge(percentage)
    print(indi)

def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    if(x>y or x<0 or y<0):
        raise ValueError
    if(y==0):
        raise ZeroDivisionError
    percentage = (x/y)*100
    return round(percentage)

def gauge(percentage):
    if (percentage>=99):
        return("F")
    elif(percentage<=1):
        return("E")
    else:
        return(f"{percentage}%")
    
if __name__ == "__main__":
        main()