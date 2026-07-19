# Check if File exists in directory.
import os
def FileDisplayContents(file):
    if os.path.exists(file):
            fobj = open(file,"r")
            data = fobj.read()
            print(f"The data from the file {file}:\n{data}\n")
        
    else:
        print(f"No such file {file} exists in the current directory")


def main():
    filename = input("Enter a file name : ")
    FileDisplayContents(filename)
    
if __name__ == "__main__":
    main() 