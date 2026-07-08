def PrintLengthOfNo(val):
    if val<0:
        val=-val
    print(len(str(val)))
        
def main():
    no = int(input("Enter a number : "))
    PrintLengthOfNo(no)
    
    
if __name__ == "__main__":
    main()