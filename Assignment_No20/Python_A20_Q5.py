import threading
def OneTo50():
    print("Numbers from 1 to 50 : ")
    for i in range(1,51):
        print(i,end = ' ')
        
    print()
    
        
def FiftyTo1():
    print("Numbers from 50 to 1 : ")
    for i in range(50,0,-1):
        print(i,end = ' ')
        
    print()
        
def main():
    
    t1 = threading.Thread(target=OneTo50)
    t2 = threading.Thread(target=FiftyTo1)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    

    print("Exit from main")
    
    
if __name__ == "__main__":
    main()