def Factorial(no):
    facto = 1
    for i in range(1,no+1):
        facto = facto * i
    print(facto)

def main():
    value= int(input("Enter a number : "))
    Factorial(value)
    
if __name__ == "__main__":
    main()