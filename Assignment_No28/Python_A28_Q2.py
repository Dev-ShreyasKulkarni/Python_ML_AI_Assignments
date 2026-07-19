# Count Words in a File.

def CountWordsInFile(file):
    try:
        fobj = open(file,'r')
        data = fobj.read()
        print(f"The data from the file : \n{data}")
        words = data.split()
        
        print(f"\nTotal Number of words in file {file} : {len(words)}") # USING BUILT_IN FUNCTION

    except FileNotFoundError as e:
        print("No such file exists")
def main():
    filename = input("Enter a file name : ")
    CountWordsInFile(filename)
    
if __name__ == "__main__":
    main()