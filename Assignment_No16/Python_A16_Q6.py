def ChkSign(val):
    if val>0:
        print("Positive Number")
    elif val<0:
        print("Negative Number")
    else:
        print("Zero")
        
def main():
    no = int(input("Enter a number : "))
    ChkSign(no)
    
if __name__ == "__main__":
    main()