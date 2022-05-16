#PlusMinus

def plusMinus(arr):
    # Write your code here
    pos_count=0
    neg_count=0
    zero_count=0
    length = len(arr)
    
    for i in range(length):
        if(arr[i]==0):
            zero_count = zero_count+1
        elif(arr[i]>0):
            pos_count = pos_count+1
        elif(arr[i]<0):
            neg_count = neg_count+1
            
    pos_ratio=pos_count/length
    neg_ratio=neg_count/length
    zero_ratio=zero_count/length
    
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)
