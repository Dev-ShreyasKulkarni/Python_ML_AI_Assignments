CheckEven = lambda value: value%2==0


def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    even_elements = list(filter(CheckEven,elements))
    if even_elements:
        print("Even elements :",even_elements)
    else:
        print("No Even elements present in the list")
    
    
if __name__ == "__main__":
    main()