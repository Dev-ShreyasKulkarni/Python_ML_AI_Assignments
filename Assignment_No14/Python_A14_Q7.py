import Numbers as Nums

def main():
    no = int(input("Enter a number : "))
    flag = Nums.IsDivsibleBy5(no)
    if flag:
        print(f"{no} is divisible by 5")
    else:
        print(f"{no} is not divisible by 5")
    
    
if __name__ == "__main__":
    main()