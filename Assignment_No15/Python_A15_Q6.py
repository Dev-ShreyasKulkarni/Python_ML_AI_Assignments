from functools import reduce

Min = lambda value1,value2:value1 if value1<value2 else value2

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    smallest_num = reduce(Min,elements)
    print("Minimum of elements :",smallest_num)
    
    
if __name__ == "__main__":
    main()