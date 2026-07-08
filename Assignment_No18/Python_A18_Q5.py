from functools import reduce
import MarvellousNum as mn

Addition = lambda x,y: x+y

def ListPrime(elements):
    sum = 0
    prime_elements = list(filter(mn.IsPrime,elements))
    if prime_elements:
        print(f"Prime list : {prime_elements}")
        sum= reduce(Addition,prime_elements)
    return sum

def main():
    elements = list()
    size = int(input("Enter the size of the list : "))
    print("Enter the elements one by one :")
    for i in range(size):
        elements.append(int(input()))
    
    print(f"Inputted list : {elements}")
    
     
    sum_prime= ListPrime(elements)
    print(f"Sum of prime elements of given list : {sum_prime}")
    
if __name__ == "__main__":
    main()
