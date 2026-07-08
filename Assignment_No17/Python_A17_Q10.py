def SumOfDigits(val):
    if val<0:
        val=-val
        
    digit = 0
    sum=0
    while val>0:
        digit=val%10
        sum+=digit
        val=val//10
        
    return sum
        
def main():
    no = int(input("Enter a number : "))
    print(f"Sum of digits in {no} : {SumOfDigits(no)}")
    
    
if __name__ == "__main__":
    main()