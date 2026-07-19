# Display line by line data in a File.

def DisplayLineByLine(file):
    try:
        fobj = open(file,'r')
        data = fobj.readlines()
        print(f"The data from the file in line by line: ")
        for line in data:
            print(line)
        
    except FileNotFoundError as e:
        print("No such file exists")
    

def main():
    filename = input("Enter a file name : ")
    DisplayLineByLine(filename)
    
if __name__ == "__main__":
    main() 