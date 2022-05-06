#ViralAdvertising

def viralAdvertising(n):
    # Write your code here
    total = 0 
    liked_people = 0 
    recipients = 5
    for i in range(n):
        liked_people = math.floor(recipients/2)
        recipients = liked_people * 3 
        total += liked_people
    return total 

"""
------
Logic:
------
1. First day company advertise to 5 people in that after floor division ie. 5/2 = 2 likes the ad so they share it with 3 friends.
2. So now 2*3 = 6 people have got advertised. this 6 people after floor division ie. 6/2 = 3 likes the ad so they share it with 3 friends
3. it goes on till nth people..
4. total people liked the ad is 2+3+... = 5 
"""
