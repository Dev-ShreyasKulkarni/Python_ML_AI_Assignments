def MarksToGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60 and marks < 75:
        print("First Class")
    elif marks >= 50 and marks < 60:
        print("Second Class")
    else:
        print("Fail")
        
def main():
    marks = int(input("Enter the marks : "))
    MarksToGrade(marks)
    
if __name__ == "__main__":
    main()