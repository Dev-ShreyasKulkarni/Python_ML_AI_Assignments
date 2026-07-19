# Read,Copy the data,Create new file and paste data in a File.
import sys
def ReadCompare(file1,file2):
    try:
        fobj1 = open(file1,'r')
        data1 = fobj1.read()
        fobj2 = open(file2,'r')
        data2 = fobj2.read()
        
        if data1 == data2:
            print("Success")
        else:
            print("Failure")
            
    except FileNotFoundError as e:
        print(f"No such file exists : {e}")
    

def main():
    try:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        ReadCompare(filename1,filename2)
    except IndexError as e:
        print(f"Invalid number of arguments : {e}")
    
if __name__ == "__main__":
    main() 