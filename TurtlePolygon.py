from turtle import *

mysize = int(input("How many sides in Polygon?"))

fillcolor('pink')
begin_fill()
for i in range(mysize):
    forward(100)
    left(360/mysize)
end_fill()
    
done()
   



    





