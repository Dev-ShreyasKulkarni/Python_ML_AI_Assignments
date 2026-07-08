import threading
def EvenList(values):
    sum = 0
    for no in values:
        if no%2==0:
            sum+=no
        
    print(f"Sum of even elements of {values} : {sum}")

def OddList(values):
    sum = 0
    for no in values:
        if no%2!=0:
            sum+=no
        
    print(f"Sum of odd elements of {values} : {sum}")
        
def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
    
    t1 = threading.Thread(target=EvenList,args=(elements,))
    t2 = threading.Thread(target=OddList,args=(elements,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("Exit from main")
    
    
if __name__ == "__main__":
    main()