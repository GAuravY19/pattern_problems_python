#reverse pyramid pattern
'''
for n=4
* * * *
* * * 
* * 
* 
'''

#solution

n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print("\n")