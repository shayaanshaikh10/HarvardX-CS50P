months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

while (True):
    try:
        date=input("Date: ").strip()

        if ("/" in date):
            month,day,year=date.split("/")
            month=int(month)
            day=int(day)
        elif " " in date:
            month,day,year=date.split(" ")
            if "," not in date:
                raise ValueError
            day=day.removesuffix(",")
            day=int(day)
            month=month.capitalize()
            month=months[month]
            month=int(month)
        else:
            raise ValueError
        if not (1<=month<=12 and 1<=day<=31):
            raise ValueError
    except:
        pass
    else:
        break


print(f"{year}-{month:02d}-{day:02d}")