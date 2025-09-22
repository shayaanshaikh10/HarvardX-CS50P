import inflect
p=inflect.engine()
name=[]
while(True):
    try:
        value=input("Name: ")
        name.append(value)
    except EOFError:
        break

names=p.join(name)
print(f"\nAdieu, adieu, to {names}")