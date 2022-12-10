
#serpinski triangle is a fractal which can be made by considering basic funaction
#which act as the basic unit of fractal and by iterating it ina correct way we can
#extend it in such a way that it would a beautiful pat6tern
#formation of statement
import math
phrase="x"
i=0
a=float(input("enter limit:"))
while(i<=a):
    g=len(phrase)
    k=0
    output=" "
    while(k<=g-1):
        if phrase[k]=="x":
            output=output+"ypxpy"
        elif phrase[k]=="y":
            output=output+"xmymx"
        elif phrase[k]=="p":
            output=output+"p"
        elif phrase[k]=="m":
            output=output+"m"
        k=k+1
    phrase=output
    i=i+1
print(phrase)#in order to check statement
#execution
ang=math.pi/3
l=len(phrase)
d=0
theta=0
x=1
y=0
xcor=[0,1]
ycor=[0,0]
while(d<=(l-1)):
    if phrase[d]=="m":
        theta=theta-ang
        x=x+math.cos(theta)
        y=y+math.sin(theta)
        ycor=ycor+[y]
        xcor=xcor+[x]
    elif phrase[d]=="p":
        theta = theta +ang
        x = x + math.cos(theta)
        y = y + math.sin(theta)
        xcor=xcor+[x]
        ycor=ycor+[y]
    d=d+1
#setting for graphical method
import matplotlib.pyplot as plt
plt.plot(xcor,ycor)
plt.show()



