from functools import reduce

Max = lambda value1,value2:value1 if value1>value2 else value2

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    largest_num = reduce(Max,elements)
    print("Maximum of elements :",largest_num)
    
    
if __name__ == "__main__":
    main()