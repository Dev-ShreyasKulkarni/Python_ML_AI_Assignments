def IsPrime(val):
    for i in range(2,(val//2)+1):
        if val%i==0:
            return False   
    else:
        return True