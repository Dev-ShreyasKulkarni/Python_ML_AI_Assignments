def CountOfDigits(no):
    if no<0:
        no = -no
    print("Count of digits is :",len(str(no)))
        
        
    
def main():
    value= int(input("Enter a number : "))
    CountOfDigits(value)
    
if __name__ == "__main__":
    main()