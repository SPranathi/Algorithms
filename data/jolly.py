
"""
A sequence of n>0 integers is called a jolly jumper if the absolute values of the difference between successive elements take on all the values 1 through n-1. 
For instance,1 4 2 3 is a jolly jumper, because the absolutes differences are 3, 2, and 1 respectively.
The defnition implies that any sequence of a single integer is a jolly jumper. 
You are to write a program to determine whether or not each of a number of sequences is a jolly jumper.
Input
Each line of input contains an integer n<=3000 followed bynintegers representing the sequence.
Output
For each line of input, generate a line of output saying `Jolly' or `Not jolly'.
Sample Input
4 1 4 2 3
5 1 4 2 -1 6
Sample Output
Jolly
Not jolly
"""
n=[int(x) for x in input().split(" ")]
t=[]
flag=0
for i in range(1,n[0]):
    d=abs(n[i]-n[i+1])
    if d<=(n[0]-1) and d>=1 and d not in t: 
        t.append(d)
    else:    
        print("Not Jolly1")
        flag=1
if flag==0:
    print("Jolly")
"""
for i in range(1,m[0]):
    q.append(abs(m[i]-m[i+1]))
    if q[i-1]<=(m[0]-1) and q[i-1]>=1: 
        pass
    else:
        print("Not Jolly2")
        break
print("Jolly")"""


        


