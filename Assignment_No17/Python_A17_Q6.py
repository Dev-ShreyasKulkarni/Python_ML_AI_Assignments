def PatternDisplay(val):
    while val>0:
        print("*\t"*val)
        val=val-1
        
def main():
    no = int(input("Enter a number : "))
    PatternDisplay(no)
    
if __name__ == "__main__":
    main()
