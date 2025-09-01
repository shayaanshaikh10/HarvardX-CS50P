greeting = input("Greeting: ").lower()
pos=greeting.find("h",0,1)

if "hello" in greeting: 
    print("$0")
elif pos==0:
    print("$20")
else:
    print("$100")
    