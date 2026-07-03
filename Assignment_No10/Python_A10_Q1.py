def MultiplicationTable(no):
    for i in range(1,11):
        print(no*i)

def main():
    value= int(input("Enter a number : "))
    MultiplicationTable(value)
    
if __name__ == "__main__":
    main()