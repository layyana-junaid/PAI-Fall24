#Layyana Junaid BS AI - 3A
# Lab 2 , task 1

#creating a program to calculate the area of a trapezoid, area of a parallelogram
#Calculate surface volume and area of a cylinder.

#function to calculate the area of trapezoid;
def AreaofTrapezoid(side1, side2, height):
    area = ((side1 + side2) * height) / 2
    print(area)

#function to calculate the area of parallelogram
def AreaofParallelogram(base, height):
    area = base * height
    print(area)

pi = 3.14
def AreaCylinder(radius, height):
    area = (2 * pi * radius * height) + (2 * pi * (radius**2))
    print(area)

def SurfaceVOlumeCylinder(radius, height):
    volume = pi * (radius**2) * height
    print(volume)

AreaofTrapezoid(2, 2, 4)
AreaofParallelogram(12, 4)
AreaCylinder(6, 8)
SurfaceVOlumeCylinder(6, 8)