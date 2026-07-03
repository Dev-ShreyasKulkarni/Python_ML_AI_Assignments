def IsPrime(no):
    if no<=1:
        print("Not Prime")
    else:
        for i in range(2,int(no/2)+1):
            if no%i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
        
    

def main():
    value= int(input("Enter a number : "))
    IsPrime(value)
    
if __name__ == "__main__":
    main()