def OddNums(no):
    for i in range(1,no+1):
        if i%2 != 0:
            print(i)

def main():
    value= int(input("Enter a number : "))
    OddNums(value)
    
if __name__ == "__main__":
    main()