from pyfiglet import Figlet
import random
import sys


figlet=Figlet()
figlet_fonts=figlet.getFonts()

if len(sys.argv)==1:
    font=random.choice(figlet_fonts)
    f= Figlet(font=font)    

elif len(sys.argv)==3 and ((sys.argv[1]=='-f') or (sys.argv[1]=='--font')):
    if not sys.argv[2] in figlet_fonts:
        sys.exit("Unsupported font type!")

    f = Figlet(font=sys.argv[2])
else:
    sys.exit("Please check your arguments!")        

user_input=input("Input: ")   
print(f.renderText(user_input))
    
