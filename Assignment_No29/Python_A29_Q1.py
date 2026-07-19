# Check if File exists in directory.
import os
def FileExists(file):

    if os.path.exists(file):
        print(f"File {file} exists in the current directory")
    else:
        print(f"No such file {file} exists in the current directory")


def main():
    filename = input("Enter a file name : ")
    FileExists(filename)
    
if __name__ == "__main__":
    main() 