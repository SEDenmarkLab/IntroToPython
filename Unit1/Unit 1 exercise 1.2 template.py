#imports (import anything you need for this question)
from math import pi


#calculate the area of a circle radius 5
#your code here


#test for you output (do not edit this)
try:
    if area(5) == pi * 5 * 5:
        print("Great! You have the correct output. The correct out put is -3.14159")
    else:
        print(f"Your output is: {area(5)}, the correct answer is -3.1416, please try again")
except Exception:
    print("if this line appears, you probably didn't import correctly")



#write a couple more tests yourself to test your code:
#for example, try different radius
