'''
The area of a triangle with sides a, b, c can be determined by Heron’s formula:
S = sqrt(s(s-a)(s-b)(s-c))
where s = ½ (a + b + c) is the semi-perimeter, or half of the triangle's perimeter.
Write a program that prompts user for 3 float values representing the sides of a triangle. Compute and display the area. Assume that input is valid, i.e. the sides are able to form a triangle. Use Google to find how to use math library function (for square root). (Hint: You need to import math module).
Example,
Enter side a: 3
Enter side b: 4
Enter side c: 5
Area is 6.0
'''

import math

def main():
    a = float (input("Enter the length of side A: "))
    b = float (input("Enter the length of side B: "))
    c = float (input("Enter the length of side C: "))
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print ("The area of the triangle is: " + str(area))

main()