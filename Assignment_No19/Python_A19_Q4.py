from functools import reduce

Add = lambda x,y: x+y
Square = lambda x: x**2
IsEven = lambda x: x%2==0

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
    
    FData = list(filter(IsEven,elements))
    print(f"Even elements : {FData}")
    
    MData = list(map(Square,FData))
    print(f"Squared Elements : {MData}")
    
    sum= reduce(Add,MData)
    print(f"Sum of filtered and mapped elements of given list : {sum}")
    
if __name__ == "__main__":
    main()
