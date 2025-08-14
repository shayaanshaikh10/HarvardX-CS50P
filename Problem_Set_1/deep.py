ans=input("What is the answer to the great question of life, the universe, and everything? ")
ans=ans.strip().lower().replace("-"," ")
if ans =="42" or ans=="forty two":
    print("Yes")
else:
    print("No")