from functools import reduce
Addition = lambda x,y: x+y

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
        
    sum= reduce(Addition,elements)
    print(f"Sum of elements of given list : {sum}")
    
if __name__ == "__main__":
    main()
