import sys
def main():
    str = input("enter a text: ")
    if not str:
        sys.exit(1)
    new_str=shorten(str)
    print(new_str)


def shorten(str):
    new_str = ""
    for i in str:
        if(i=="a"or i=="e"or i=="i"or i=="o"or i=="u"or i=="A"or i=="E"or i=="I"or i=="O"or i=="U"):
            continue
        else:
            new_str = new_str+i
    return new_str

if __name__ =="__main__":
    main()
