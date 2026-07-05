IsDivisbleBy3And5 = lambda value: value%3==0 and value%5==0

def main():
    elements = list()
    size = int(input("Enter a number of elements : "))
    for i in range(size):
        no = int(input(f"Enter the number {i+1}: "))
        elements.append(no)
        
    print("Inputted elements :",elements)
    
    elements_divsibleby_3_5 = list(filter(IsDivisbleBy3And5,elements))
    if elements_divsibleby_3_5:
        print("Elements divisble by 3 and 5 elements :",elements_divsibleby_3_5)
    else:
        print("No elements divisble by 3 and 5 present in the list")
    
    
if __name__ == "__main__":
    main()