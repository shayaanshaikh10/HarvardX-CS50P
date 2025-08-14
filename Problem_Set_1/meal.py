def main():
    time=input("enter the time: ")
    point_time=convert(time)
    # print(point_time)
    if 7<=point_time<=8:
        print("breakfast time")
    elif 12<=point_time<=13:
        print("lunch time")
    elif 18<=point_time<=19:
        print("dinner time")

def convert(time):
    hr,min = time.split(":")
    hr=float(hr)
    min=float(min)
    min=min/60
    point_time=round(hr+min,2)
    return point_time

if __name__ == "__main__":
    main()