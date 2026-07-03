def IsDivisble(no):
    if no%3==0 and no%5==0:
        print(no,"is Divisible by 3 and 5")
    elif no%3==0 and no%5!=0:
        print(no,"is Divisible by 3 but not by 5")
    elif no%3!=0 and no%5==0:
        print(no,"is Divisible by 5 but not by 3")
    elif no%3!=0 and no%5!=0:
        print(no,"is neither divisible by 3 nor by 5")
    
def main():
    value = int(input("Enter a number : "))
    IsDivisble(value)
    
if __name__ == "__main__":
    main()