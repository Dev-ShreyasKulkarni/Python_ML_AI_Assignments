import Arithmetic as arm

def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))
    
    print(f"Addition of {no1} and {no2} : {arm.Add(no1,no2)}")
    print(f"Subtraction of {no1} and {no2} : {arm.Sub(no1,no2)}")
    print(f"Multiplication of {no1} and {no2} : {arm.Mult(no1,no2)}")
    print(f"Division of {no1} and {no2} : {arm.Div(no1,no2):.3f}")
    
if __name__ == "__main__":
    main()
