#output pattern :- 
''' for n = 4, m=5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

#solution :- 

n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print("\n")
    
    
