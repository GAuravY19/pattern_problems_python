# Hollow diamond pattern 

""" 
for n = 4 
   *
  * *
 *   *
*     *
 *   *
  * *
   * 
"""

n = int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range((i*2)-1):
        if j == (n-i)+1 or j == (i*2)-1:
            print("*", end="")
    print("\n")