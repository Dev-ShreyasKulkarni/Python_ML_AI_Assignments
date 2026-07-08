def IsDivisibleBy5(val):
    return val%5==0
        
def main():
    no = int(input("Enter a number : "))
    ret = IsDivisibleBy5(no)
    print(ret)
    
if __name__ == "__main__":
    main()