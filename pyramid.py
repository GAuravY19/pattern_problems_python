#pyramid pattern
'''
for n=4
* 
* *
* * * 
* * * *
'''

#solution

n = int(input())
j = n
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print("\n")