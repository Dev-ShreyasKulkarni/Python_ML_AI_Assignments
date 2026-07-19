# Read,Copy the data,Create new file and paste data in a File.
import sys
def ReadCopyPasteToNewFile(file):
    try:
        fobj1 = open(file,'r')
        data = fobj1.read()
        print(f"The data from the file {file}:\n{data}\n")
        
        fobj2= open("CopiedDemo.txt",'w')
        fobj2.write(data)
        print(f"File CopiedDemo.txt generated successfully with copied data written on it.")
        
    except FileNotFoundError as e:
        print(f"No such file exists : {file}")
    

def main():
    filename = sys.argv[1]
    ReadCopyPasteToNewFile(filename)
    
if __name__ == "__main__":
    main() 