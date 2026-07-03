ToBinary =  lambda x: bin(x)
def main():
    num = int(input("Enter the number : "))
    print("Binary eqvivalent of",num,":",ToBinary(num))
    
if __name__ == "__main__":
    main()