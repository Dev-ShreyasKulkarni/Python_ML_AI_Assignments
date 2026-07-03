def AreaOfRectangle(len,wid):
    if len <=0 or wid<=0:
        print("Length or Width cannot be zero or negative")
    else:
        print("Area of rectangle is :",len*wid)
    
def main():
    length = int(input("Enter the length of rectangle : "))
    width = int(input("Enter the width of rectangle : "))
    AreaOfRectangle(length,width)
    
if __name__ == "__main__":
    main()