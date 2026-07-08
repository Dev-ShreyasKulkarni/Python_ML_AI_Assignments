import threading
def Small(word):
    small_chars = [ch for ch in word if ch.islower()]
    print(f"Thread ID : {threading.get_ident()}, Thread Name : {threading.current_thread().name}")
    print(f"Count of lowercase characters in {word} : {len(small_chars)}\n")

def Capital(word):
    cap_chars = [ch for ch in word if ch.isupper()]
    print(f"Thread ID : {threading.get_ident()}, Thread Name : {threading.current_thread().name}")
    print(f"Count of uppercase characters in {word} : {len(cap_chars)}\n")

        
def main():
    word = input("Enter a string : ")
    print(f"Inputted string : {word}")
    
    t1 = threading.Thread(target=Small,args=(word,))
    t2 = threading.Thread(target=Capital,args=(word,))
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f"Thread ID : {threading.get_ident()}, Thread Name : {threading.current_thread().name}")

    print("Exit from main")
    
    
if __name__ == "__main__":
    main()