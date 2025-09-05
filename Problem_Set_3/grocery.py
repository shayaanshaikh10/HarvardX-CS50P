list={}
while (True):
    try:
        item=input("").upper()
        if(item not in list):
            list[item]=int(1)
        else:
            list[item]=list[item]+1
    except EOFError:
        break

sorted_keys=sorted(list)

for item in sorted_keys:
    count = list[item] 
    print(f"{count} {item}")
    