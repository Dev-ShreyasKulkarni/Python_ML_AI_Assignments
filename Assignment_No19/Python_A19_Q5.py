from functools import reduce

Add = lambda x,y: x+y
MultiplyBy2 = lambda x: x*2
Max_Num = lambda x,y: x if x>y else y

def IsPrime(val):
    for i in range(2,(val//2)+1):
        if val%i==0:
            return False   
    else:
        return True

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
    
    FData = list(filter(IsPrime,elements))
    print(f"Prime elements : {FData}")
    
    MData = list(map(MultiplyBy2,FData))
    print(f"Doubled Elements : {MData}")
    
    max= reduce(Max_Num,MData)
    print(f"Maximum of filtered and mapped elements of given list : {max}")
    
if __name__ == "__main__":
    main()
