# Palimdromic Pattern 

'''
for n=4
   1
  2 2
 3 3 3
4 4 4 4 
'''

n = int(input())
print("-----------------")

for i in range(1, n+1):
    for j in range(n-i):
        print(" ",end="")
    
    for j in range(1, i+1):
        print(i, end=" ")
    
    print("\n")
    