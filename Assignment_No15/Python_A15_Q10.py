CheckEven = lambda value: value%2==0


def main():
    elements = list()
    size = int(input("Enter the number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
    
    print("Inputted elements :",elements)
    
    Count_EvenNums = len(list(filter(CheckEven,elements)))
    print("No of even elements :",Count_EvenNums)

if __name__ == "__main__":
    main()