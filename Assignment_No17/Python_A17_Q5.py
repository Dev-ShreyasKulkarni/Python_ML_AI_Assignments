def IsPrime(val):
    for i in range(2,(val//2)+1):
        if val%i==0:
            print("It is not a Prime Number")
            break   
    else:
        print("It is a Prime Number")
    
def main():
    no = int(input("Enter a number : "))
    IsPrime(no)
    
if __name__ == "__main__":
    main()
