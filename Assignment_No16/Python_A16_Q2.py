def ChkNum(val):
    if val%2==0:
        print("Even number")
    else:
        print("Odd number")
        
def main():
    no = int(input("Enter a number : "))
    ChkNum(no)
    
if __name__ == "__main__":
    main()