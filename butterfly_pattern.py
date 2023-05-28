# butterfly pattern
'''
*             *
* *         * *
* * *     * * *
* * * * * * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
'''

#solution

n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    space = 2*n - (2*i)
    for j in range(space):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("\n")

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    space = 2*(n-i)
    for j in range(space):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("\n")