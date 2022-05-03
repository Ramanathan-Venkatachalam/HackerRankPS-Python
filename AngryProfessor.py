#AngryProfessor

def angryProfessor(k, a):
    length = len(a)
    count = 0
    for i in range(length):
        if(a[i] <= 0):
            count = count+1
    if(count >= k):
        return "NO"
    return "YES"   
