# x= int(input("value of x "))
# y= int(input("value of y "))

# if x<y:
#     print("x is less than y")
# elif x>y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

# marks=float(input("enter the marks "))

# if marks<=100 and marks>=90:
#     print("A")
# elif marks<90 and marks>=80:
#     print("B")
# elif marks<=79 and marks>=70:
#     print("C")

#using modulo
# def main ():
#     x= int(input("enter the value of x "))
#     if is_even(x):
#         print("even")
#     else:
#         print("odd")

# def is_even(x):
#     return x%2==0

# main()

#using match
# day = input("enter the day ")

# match day:
#     case "mon" | "tue" |"wed" |"thu" |"fri" :
#         print("weekday")
#     case "sat" |"sun" :
#         print("weekend")
#     case _:
#         print("please enter any one of seven days")

#using while keyword
# i=0
# while i<3:
#     print("meow")
#     i +=1

#using for keyword
# for i in range(3):
#     print("meow")


# while True:
#     n=int(input("enter the value of n (+): "))
#     if n>0:
#         break

# for i in range(n):
#     print("meow")

#printing meow n times using functions
# def main():
#     n=get_number()
#     meow(n)

# def get_number():
#     while True:
#         n=int(input("enter a number: "))
#         if n>0:
#             break
#     return n


# def meow(n):
#     for i in range(n):
#         print("meow")

# main()

#printing the content of a list using for loop
# students=["hermoine","harry","ro"]
# for student in students:
#     print(student)

#using len keyword
# dc=["batman","superman","robbin"]

# for i in range(len(dc)):
#     print(i+1,dc[i])

#dictionary
# dc={
#     "batman":"batcave",
#     "superman":"universe",
#     "robbin":"gotham",
#     }

# for hero in dc:
#     print(dc[hero])

#list of dictionary
# dc=[
#     {"name":"batman","place":"gotham","age":"34"},
#     {"name":"superman","place":"universe","age":"51"},
# ]

# for hero in dc:
#     print(f"{hero["name"]}, {hero["place"]}, {hero["age"]}")

#nested loops(printing square)
# def main():
#     print_square(5)

# def print_square(size):
#     for i in range(size):
#         print_row(size)
#         print()

# def print_row(size):
#     for i in range(size):
#         print("#",end="")

# main()
