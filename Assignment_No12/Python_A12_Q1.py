def IsVowel(char):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if char in vowels:
        print("Vowel")
    else:
        print("Not a Vowel")
    
def main():
    char = input("Enter a character : ")
    IsVowel(char)
    
if __name__ == "__main__":
    main()