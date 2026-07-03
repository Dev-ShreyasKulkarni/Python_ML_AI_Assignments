def SumOfDigits(no):
    if no<0:
        no = -no
    sum = 0
    val = 0
    for i in range(len(str(no))):
        val = no%10
        no =int(no/10)
        
        sum= sum + val
    
    print("Sum of digits :",sum)
        
        
    
def main():
    value= int(input("Enter a number : "))
    SumOfDigits(value)
    
if __name__ == "__main__":
    main()