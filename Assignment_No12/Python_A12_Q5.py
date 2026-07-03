def PrintNumsReverseOrder(val):
    for i in range(val,0,-1):
        print(i)
    
def main():
    no = int(input("Enter a number : "))
    PrintNumsReverseOrder(no)
    
if __name__ == "__main__":
    main()
    