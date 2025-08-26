def main():
    str=input("Input: ")
    remove_vowel(str)

def remove_vowel(str):
    print("Output:",end="")
    for i in str:
        if i=="A" or i=="a" or i=="E" or i=="e" or i=="I" or i=="i" or i=="O" or i=="o" or i=="U" or i=="u":
            continue
        else:
            print(i,end="") 

main()