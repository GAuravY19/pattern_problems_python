# half pyramid using numbers pattern
'''
for n=4
1
2 2 
3 3 3 
4 4 4 4
'''

#solution

n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print("\n")