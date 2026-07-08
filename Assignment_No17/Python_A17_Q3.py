Factorial = lambda val : val*Factorial(val-1) if val>0 else 1
    
        
def main():
    no = int(input("Enter a number : "))
    print(f"Factorial of {no} is : {Factorial(no)}")
    
if __name__ == "__main__":
    main()
