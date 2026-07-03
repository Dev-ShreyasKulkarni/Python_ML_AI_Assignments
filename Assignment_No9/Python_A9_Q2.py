def ChkGreater(no1,no2):
    if no1 > no2 :
        print(no1,"is greater")
    elif no2 > no1 :
        print(no2,"is greater")
    else:
        print("Both are equal")
    
def main():
    value1 = int(input("Enter the first number : "))
    value2 = int(input("Enter the second number : "))

    ChkGreater(value1,value2)
    
if __name__ == "__main__":
    main()