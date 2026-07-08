def PatternDisplay(val):
    for i in range(val):
        print("*\t"*val)
        
def main():
    no = int(input("Enter a number : "))
    PatternDisplay(no)
    
if __name__ == "__main__":
    main()
