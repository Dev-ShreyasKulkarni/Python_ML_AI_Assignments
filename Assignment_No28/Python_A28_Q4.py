# Read,Copy the data,Create new file and paste data in a File.

def ReadCopyPasteToNewFile(file,newfile):
    try:
        fobj1 = open(file,'r')
        data = fobj1.read()
        print(f"The data from the file {file}:\n{data}\n")
        
        fobj2= open(newfile,'w')
        fobj2.write(data)
        print(f"File {newfile} generated successfully with copied data written on it.")
        
    except FileNotFoundError as e:
        print(f"No such file exists : {file}")
    

def main():
    filename = input("Enter a name of first file to copy contents from : ")
    newfilename = input("Enter a name of new file to paste contents to : ")
    ReadCopyPasteToNewFile(filename,newfilename)
    
if __name__ == "__main__":
    main() 