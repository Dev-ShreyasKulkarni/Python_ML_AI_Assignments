from functools import reduce

Sum= lambda value1,value2:value1+value2

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    sum = reduce(Sum,elements)
    print("Sum of elements :",sum)
    
    
if __name__ == "__main__":
    main()