import sys
import pyfiglet

f=pyfiglet.Figlet()
all_fonts=f.getFonts()



if len(sys.argv)!=3 and len(sys.argv)!=1:
    sys.exit("error")

if len(sys.argv)==3:
    if sys.argv[2] not in all_fonts:
        sys.exit("error")
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit("error")

input=input("Input: ")
if len(sys.argv)==3:
    f=pyfiglet.figlet_format(input,font=sys.argv[2])
else:
    f=pyfiglet.figlet_format(input)

print(f)