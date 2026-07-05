Square= lambda value:value*value

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    squared_elements = list(map(Square,elements))
    print("Squared elements :",squared_elements)
    
    
if __name__ == "__main__":
    main()