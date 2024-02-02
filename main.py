import math
import replit
def triside(x):
    return x * math.sqrt(3)
def triperi(x):
    return x * math.sqrt(3) * 3
def triarea(x):
    return x ** 2 * (math.sqrt(3)/4)
def cirperi(x):
    return math.pi * 2 * x
def cirarea(x):
    return math.pi * x ** 2
print("Radius of circle in centimeters?")
try:
    r = float(input())
except:
    exit("Invalid input. Radius must be a number greater than zero.") 
if r > 0:
    triside = triside(r)
    triperi = triperi(r)
    triarea = triarea(r)
    cirperi = cirperi(r)
    cirarea = cirarea(r)
    triside_ans = "The length of one side of the inscribed equilateral triangle is %.2f cm (2d.p.)."
    triperi_ans = "The perimeter of the inscribed equilateral triangle is %.2f cm (2d.p.)."  
    triarea_ans = "The area of the inscribed equilateral triangle is %.2f cm^2 (2d.p.)."
    cirperi_ans = "The circumference of the circle is %.2f cm (2d.p.)."
    cirarea_ans = "The area of the circle is %.2f cm^2 (2d.p.)."
    replit.clear()
    print(triside_ans % triside)
    print(triperi_ans % triperi)
    print(triarea_ans % triarea)
    print(cirperi_ans % cirperi)
    print(cirarea_ans % cirarea)
    input("\n\nPress Enter to exit.")
    quit()
else:
    exit("Invalid Input. Radius must be a number greater than zero.")