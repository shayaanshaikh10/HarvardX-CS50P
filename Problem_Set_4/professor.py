import random


def main():
    score=int(0)

    level=get_level()
    for i in range(0,10):
        x=generate_integer(level)
        y=generate_integer(level)
        for i in range(0,3):
            answer=int(input(f"{x} + {y} = "))
            if answer!=x+y:
                if i==2:
                    print(f"{x} + {y} = {x+y}")
                else:
                    print("EEE")
                    continue
            elif answer==x+y:
                score=score+1
                break

    print(f"Score: {score}")


def get_level():
    while(True):
        try:
            level=int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        return x
    elif level==2:
        x=random.randint(10,99)
        return x
    elif level==3:
        x=random.randint(100,999)
        return x


if __name__ == "__main__":
    main()