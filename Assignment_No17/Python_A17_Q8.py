def PatternDisplay(val):
    for i in range(1,val+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
        
        
def main():
    no = int(input("Enter a number : "))
    PatternDisplay(no)
    
if __name__ == "__main__":
    main()
