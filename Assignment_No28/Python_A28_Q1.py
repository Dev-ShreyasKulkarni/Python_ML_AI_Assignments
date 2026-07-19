# Count Lines in a File.

def CountDataLines(file):
    try:
        fobj = open(file,'r')
        data = fobj.read()
        print(f"The data from the file : \n{data}")
        fobj.seek(0)
        print(f"\nTotal Number of lines in file {file} : {len(fobj.readlines())}") # USING BUILT_IN FUNCTION
    except FileNotFoundError as e:
        print("No such file exists")
        
def main():
    filename = input("Enter a file name : ")
    CountDataLines(filename)
    
if __name__ == "__main__":
    main()