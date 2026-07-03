def IsPerfectNum(no):
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum+=i
            
    if sum==no:
        print("Perfect Number")
    else:
        print("Not a perfect Number")
        
def main():
    num = int(input("Enter a number : "))
    IsPerfectNum(num)
    
if __name__ == "__main__":
    main()