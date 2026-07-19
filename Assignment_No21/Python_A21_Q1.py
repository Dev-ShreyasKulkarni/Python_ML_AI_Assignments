import threading

def IsPrime(values):
    prime = list()
    for val in values: 
        for i in range(2,(val//2)+1):
            if val%i==0:
                break 
        continue
    else:
        prime.append(val)
    
def IsNonPrime(values):
    non_prime = list()
    for val in values: 
        for i in range(2,(val//2)+1):
            if val%i==0:
                non_prime.append(val)
        else:
            return False
    
def main():
    t1 = threading.Thread(target=IsPrime)
    t2 = threading.Thread(target=First10Odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()