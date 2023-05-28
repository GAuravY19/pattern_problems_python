#number pyramid
'''
    1
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5
'''

#solution

n = int(input())

for i in range(n):
    for j in range(n):
        if (j<n-i-1):
            print(" ", end=" ")
    for j in range(i):
        print(i, end=" ")
    print("\n")