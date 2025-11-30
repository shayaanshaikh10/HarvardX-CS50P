def main ():
    greeting = input("greetings: ").lower().strip()
    print(value(greeting))

def value(greeting):
    if greeting.startswith("hello"):
        return int(0)
    elif greeting[0]=="h":
        return int(20)
    else:
        return int(100)
    
if __name__ =="__main__":
    main()