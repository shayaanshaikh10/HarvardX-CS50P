def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_len_valid(s) and is_sign(s) and is_middle(s) and first_two(s) :
        return True
    else:
        return False

def first_two(s):
    return s[0:2].isalpha()


def is_len_valid(s):
    if 2<=len(s)<=6:
        return True
    else:
        return False

def is_sign(s):
    for i in s:
        if i==" " or i=="_" or i==".":
            return False
    return True

def is_middle(s):
    for index,char in enumerate(s):
        if char.isdecimal():
            if char=="0":
                return False
            else:
                return s[index:len(s)].isdecimal()
    return True

if __name__=="__main__":
    main()
