from Numbers import Addition

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    print(f"Sum of {no1},{no2} is {Addition(no1,no2)}")
    
    
if __name__ == "__main__":
    main()