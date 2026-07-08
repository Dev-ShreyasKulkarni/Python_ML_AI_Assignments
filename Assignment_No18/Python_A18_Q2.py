from functools import reduce
Max_Num = lambda x,y: x if x>y else y

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
        
    max= reduce(Max_Num,elements)
    print(f"Maximum number of elements of given list : {max}")
    
if __name__ == "__main__":
    main()
