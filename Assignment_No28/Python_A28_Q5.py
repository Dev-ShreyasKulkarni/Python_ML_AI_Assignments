# Read,Copy the data,Create new file and paste data in a File.

def FindWordInFile(file,word):
    try:
        fobj1 = open(file,'r')
        data = fobj1.read()
        print(f"The data from the file {file}:\n{data}\n")
        
        words = data.split()
        if word in words:
            print(f"The word {word} is present in the file")
        else :
            print(f"The word {word} is not present in the file")
    
    except FileNotFoundError as e:
        print(f"No such file exists : {file}")
    

def main():
    filename = input("Enter a name of file : ")
    word = input("Enter a word to search in file : ")
    FindWordInFile(filename,word)
    
if __name__ == "__main__":
    main() 