def SumOfFirstN_Nums(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    print(sum)

def main():
    value= int(input("Enter a number : "))
    SumOfFirstN_Nums(value)
    
if __name__ == "__main__":
    main()