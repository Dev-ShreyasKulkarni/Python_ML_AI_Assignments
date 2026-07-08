from functools import reduce

Product = lambda x,y: x*y
IncrementBy1 = lambda x: x+10
IS_70_TO_90 = lambda x: x>=70 and x<=90

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
    
    FData = list(filter(IS_70_TO_90,elements))
    print(f"Elements >=70 AND <=90 : {FData}")
    
    MData = list(map(IncrementBy1,FData))
    print(f"Incremented by 1 : {MData}")
    
    product= reduce(Product,MData)
    print(f"Product of filtered and mapped elements of given list : {product}")
    
if __name__ == "__main__":
    main()
