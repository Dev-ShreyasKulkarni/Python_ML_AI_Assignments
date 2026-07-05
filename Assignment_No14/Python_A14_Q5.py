import Numbers as Nums

def main():
    no = int(input("Enter a number : "))
    flag = Nums.IsEven(no)
    if flag:
        print(f"{no} is an even number")
    else:
        print(f"{no} is not an even number")
    
    
if __name__ == "__main__":
    main()