def CountOccurence(values,element):
    count = 0
    for no in values:
        if no == element:
            count += 1
    return count


def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
    
    search = int(input("Enter the number to search : "))
        
    cnt= CountOccurence(elements,search)
    print(f"Occurence of element in the given list : {cnt}")
    
if __name__ == "__main__":
    main()