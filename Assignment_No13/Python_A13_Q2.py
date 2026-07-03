from math import pi

def AreaOfCircle(rad):
    if rad <=0 :
        print("Radius cannot be zero or negative")
    else:
        print("Area of rectangle is :",pi*rad*rad)
    
def main():
    radius = int(input("Enter the radius of circle : "))
    AreaOfCircle(radius)
    
if __name__ == "__main__":
    main()