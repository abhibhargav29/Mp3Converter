def isPalindrome(x):
    if(x<0):
        return False
    elif(x==0):
        return True
    digits=[]
    while(x!=0):
        digits.append(x%10)
        x=x//10
    for i in range(int(ceil(len(digits)/2))):
        if(digits[i]!=digits[-(i+1)]):
            return False
    return True

x=int(input())
print(isPalindrome(x))
