import threading
def First10Even():
    i = 0
    no = 2
    while i<10:
        print(no) 
        no+=2
        i+=1

def First10Odd():
    i = 0
    no = 1
    while i<10:
        print(no) 
        no+=2
        i+=1
        
def main():
    t1 = threading.Thread(target=First10Even)
    t2 = threading.Thread(target=First10Odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    
if __name__ == "__main__":
    main()