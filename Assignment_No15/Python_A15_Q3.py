CheckOdd = lambda value: value%2!=0

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    odd_elements = list(filter(CheckOdd,elements))
    if odd_elements:
        print("Odd elements :",odd_elements)
    else:
        print("No Odd elements present in the list")
    
    
if __name__ == "__main__":
    main()