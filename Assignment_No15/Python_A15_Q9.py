from functools import reduce

Product = lambda value1,value2:value1*value2

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        if no == 0:
            print("Entered element is 0. Hence, product of elements is 0")
            return
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    product = reduce(Product,elements)
    print("Product of elements :",product)
    
    
if __name__ == "__main__":
    main()