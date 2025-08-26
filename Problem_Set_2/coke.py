due=int(50)
total_added=int(0)

while due>0:
    print(f"Amount Due: {due}")
    insert=int(input("Insert Coin: "))
    if insert!=25 and insert!=10 and insert!=5:
        continue
    total_added=total_added+insert
    due=due-insert
    if total_added>=50:
        change=total_added-50
        print(f"Change Owed: {change}")