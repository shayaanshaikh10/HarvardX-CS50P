item = input("Item: ").title()
cals_data = {"Apple":130,"Avocado":50,"Sweet Cherries":100,"Pear":100,"Kiwifruit":90}
for i in cals_data:
    if i==item:
        print(cals_data[i])


