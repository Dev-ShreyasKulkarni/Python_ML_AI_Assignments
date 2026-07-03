def Factors(val):
    for i in range(1,val+1):
        if val%i==0 :
            print(i)
    
def main():
    no = int(input("Enter a number : "))
    Factors(no)
    
if __name__ == "__main__":
    main()