def FactorSum(val):
    sum=0
    for i in range(1,(val//2)+1):
        if val%i==0:
            sum+=i    
        
    return sum
    
def main():
    no = int(input("Enter a number : "))
    print(f"Sum of factors of {no} is : {FactorSum(no)}")
    
if __name__ == "__main__":
    main()
