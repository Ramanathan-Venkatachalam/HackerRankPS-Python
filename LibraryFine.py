#LibraryFine

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if(y1 > y2):
        fineamount = 10000 #4
    elif(y1 == y2 and m1 > m2):
        fineamount = 500 * (m1-m2) #3
    elif((y1 < y2) or (y1 <= y2 and m1 <= m2 and d1 <= d2) or (y1 == y2 and m1 < m2)): 
        fineamount = 0 #1
    else:
        fineamount = 15 * (d1 - d2)  #2
    return fineamount
