def ReverseNo(no):
    num = no
    
    if no<0:
        no=-no
    revNo = 0
    
    while no>0:
        digit = no%10
        revNo = revNo * 10 + digit
        no = int(no/10)
        
    if num == revNo:
        print("Palindrome")
    else:
        print("Palindrome")
        
        
    
def main():
    value= int(input("Enter a number : "))
    ReverseNo(value)
    
if __name__ == "__main__":
    main()