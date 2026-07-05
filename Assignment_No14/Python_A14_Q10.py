from Numbers import LargestOfThree

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    no3 = int(input("Enter third number : "))
    print(f"Largest number out of {no1},{no2},{no3} is {LargestOfThree(no1,no2,no3)}")
    
    
if __name__ == "__main__":
    main()      