# Count Words in a File.

def FrequencyInFile(file,word_string):
    try:
        fobj = open(file,'r')
        data = fobj.read()
        print(f"The data from the file : \n{data}")
        
        words = data.split()
        cnt = 0
        for word in words:
            if word == word_string:
                cnt+=1
        
        print(f"\nFrequency of word {word_string} in file {file} : {cnt}") # USING BUILT_IN FUNCTION

    except FileNotFoundError as e:
        print("No such file exists")
def main():
    filename = input("Enter a file name : ")
    string_word = input("Enter a string : ")

    FrequencyInFile(filename,string_word)
    
if __name__ == "__main__":
    main()