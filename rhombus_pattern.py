# rhombus pattern

'''
   ****
  ****
 ****
****
'''

#solution

n = int(input())


for i in range(n):
    for j in range(n):
        if (j<n-i-1):
            print(" ", end=" ")
    for j in range(n):
        print("*", end=" ")

    print("\n")