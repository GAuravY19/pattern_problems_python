#1_0_pyramid pattern

'''
1
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1
'''

#solution

n = int(input())

for i in range(1,n+1):
    for j in range(i):
        if ((i+j)%2 == 0):
            print(0, end=" ")
        else:
            print(1, end=" ")
    print("\n")


