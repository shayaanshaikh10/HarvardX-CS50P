def main():
    camelCase=input("camelCase: ")
    convert(camelCase)

def convert(camelCase):
    print("snake_case:",end="")
    for i in camelCase:
        if i.isupper():
            print("_",end="")
            i=i.lower()
            print(i,end="")
        else:
            print(i,end="")

main()