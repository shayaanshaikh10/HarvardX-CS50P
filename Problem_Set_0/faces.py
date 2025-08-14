def main ():
    x=input("Enter the text: ")
    convert(x)

def convert(x):
    y=x.replace(":)","🙂").replace(":(","🙁")
    print(f"The output: {y}")

main ()