LongerThan5 = lambda string: len(string)>5


def main():
    elements = list()
    size = int(input("Enter a number of strings : "))
    for i in range(size):
        string = input(f"Enter the string number {i+1}: ")
        elements.append(string)
        
    print("Inputted strings :",elements)
    
    strings_longer_than_5 = list(filter(LongerThan5,elements))
    if strings_longer_than_5:
        print("Strings above length 5:",strings_longer_than_5)
    else:
        print("No strings above length 5 present in the list")
    
    
if __name__ == "__main__":
    main()