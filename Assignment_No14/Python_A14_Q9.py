from Numbers import Multiplication

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    print(f"Product of {no1},{no2} is {Multiplication(no1,no2)}")
    
    
if __name__ == "__main__":
    main()