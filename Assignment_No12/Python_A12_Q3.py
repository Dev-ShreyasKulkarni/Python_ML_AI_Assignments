Addition = lambda no1,no2 : no1+no2
Substraction = lambda no1,no2 : no1-no2
Multiplication = lambda no1,no2 : no1*no2
Division = lambda no1,no2 : no1/no2
    
def main():
    no1 = int(input("Enter a number : "))
    no2 = int(input("Enter a number : "))
    print("Addition is :",Addition(no1,no2))
    print("Substraction is :",Substraction(no1,no2))
    print("Multiplication is :",Multiplication(no1,no2))
    print("Division is :",Division(no1,no2))
    
if __name__ == "__main__":
    main()