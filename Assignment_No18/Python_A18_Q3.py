from functools import reduce
Min_Num = lambda x,y: x if x<y else y

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
        
    min= reduce(Min_Num,elements)
    print(f"Minimum number of elements of given list : {min}")
    
if __name__ == "__main__":
    main()
