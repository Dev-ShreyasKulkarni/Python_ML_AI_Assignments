import Numbers as Nums

def main():
    no = int(input("Enter a number : "))
    flag = Nums.IsOdd(no)
    if flag:
        print(f"{no} is an odd number")
    else:
        print(f"{no} is not an odd number")
    
    
if __name__ == "__main__":
    main()