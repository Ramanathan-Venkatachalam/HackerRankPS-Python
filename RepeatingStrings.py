#RepeatingStrings

def repeatedString(s, n):
    # Write your code here
    length = len(s) 5
    count = 0
    
    for i in range(length):
        if s[i]=='a':
            count+=1

    count=int(n/length)*count
    temp=n%length
    
    for i in range(temp):
        if s[i]=='a':
            count+=1
            
    return count
