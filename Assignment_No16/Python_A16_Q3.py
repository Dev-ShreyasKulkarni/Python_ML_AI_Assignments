def Add(val1,val2):
    return val1+val2
        
def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))

    ret = Add(no1,no2)
    print(f"Addition of {no1} and {no2} is {ret}")
    
if __name__ == "__main__":
    main()