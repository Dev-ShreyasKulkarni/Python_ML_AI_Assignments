import threading
def SumEvenFactors(no):
    sum = 0
    for i in range(1,no//2+1):
        if no%i==0 and i%2==0:
            sum+=i
        
    print(f"Sum of even factors of {no} : {sum}")

def SumOddFactors(no):
    sum = 0
    for i in range(1,no//2+1):
        if no%i==0 and i%2!=0:
            sum+=i
        
    print(f"Sum of odd factors of {no} : {sum}")
        
def main():
    no = int(input("Enter a number : "))
    t1 = threading.Thread(target=SumEvenFactors,args=(no,))
    t2 = threading.Thread(target=SumOddFactors,args=(no,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("Exit from main")
    
    
if __name__ == "__main__":
    main()